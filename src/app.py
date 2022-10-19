import os
from dotenv import load_dotenv

import requests
from requests.adapters import HTTPAdapter, Retry

from flask import Flask, request, render_template, abort

from db import Database

load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
db = Database(
    os.getenv("DBNAME"),
    os.getenv("LOGIN"),
    os.getenv("PASSWORD"),
    os.getenv("URL"),
    os.getenv("PORT"),
)

session = requests.Session()
retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[400])
session.mount("http://", HTTPAdapter(max_retries=retries))


def render(content: dict, from_cache: bool = False) -> str:
    metadata = session.get(content["metaplex"]["metadataUri"]).json()

    nft = {
        "address": content.get("mint", ""),
        "name": metadata.get("name", ""),
        "description": metadata.get("description", ""),
        "collection": metadata.get("symbol", "")
        + (
            " | "
            if metadata.get("symbol", "")
            and (
                metadata.get("collection", {"name": ""})["name"]
                or metadata.get("external_url", "")
            )
            else ""
        )
        + metadata.get("collection", {"name": ""})["name"]
        or metadata.get("external_url", ""),
        "image": metadata.get("image", "../static/placeholder.png"),
        "url": metadata.get("external_url", ""),
        "attributes": metadata.get("attributes", ""),
        "from_cache": from_cache,
    }

    return render_template("nft.html", nft=nft)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    address = request.args.get("address")

    if cached := db.find(address):
        return render(cached, from_cache=True)

    print(f"{address} not in cache")
    headers = {"accept": "application/json", "X-API-Key": API_KEY}
    response = session.get(
        f"https://solana-gateway.moralis.io/nft/mainnet/{address}/metadata",
        headers=headers,
    )

    print(f"Moralis returned code {response.status_code}")
    if response.status_code != 200:
        abort(404)

    if not db.insert(address, response.json()):
        print("Error occured while saving")

    return render(response.json())


@app.errorhandler(404)
def page_not_found(error):
    return render_template("notfound.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
