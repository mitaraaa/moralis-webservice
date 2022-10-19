from flask.testing import FlaskClient

import sys

sys.path.append(".")
sys.path.append("./src")

from src.app import app

client = app.test_client()


def test_valid_nft():
    """
    GIVEN a NFT token

    WHEN GET Request invoked

    THEN check for data being returned correctly
    """
    response = client.get(
        "/search?address=An36Gv8UFt6YW4rGdtdZu3BKWqJQVsFwRb5haRJwF2cK"
    )
    assert b"DeGod #737" in response.data

    response = client.get(
        "/search?address=EFqtEKp7SNPVYBBXShg6A2jR8xrNnvFypZpTSEEnKD3V"
    )
    assert b"SOLGods 3846" in response.data
