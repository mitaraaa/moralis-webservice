# Moralis Python Web Service

## Installation

```sh
pip install -r requirements.txt
```

## Usage

```sh
python src/app.py
```

## Examples

```
GET 
/search?address=An36Gv8UFt6YW4rGdtdZu3BKWqJQVsFwRb5haRJwF2cK HTTP/1.1
```

```json
{
  "mint": "An36Gv8UFt6YW4rGdtdZu3BKWqJQVsFwRb5haRJwF2cK",
  "standard": "metaplex",
  "name": "DeGod #737",
  "symbol": "DGOD",
  "metaplex": {
    "metadataUri": "https://metadata.degods.com/g/736.json",
    "updateAuthority": "AxFuniPo7RaDgPH6Gizf4GZmLQFc4M5ipckeeZfkrPNn",
    "sellerFeeBasisPoints": 0,
    "primarySaleHappened": 1,
    "owners": [
      {
        "address": "8RMqBV79p8sb51nMaKMWR94XKjUvD2kuUSAkpEJTmxyx",
        "verified": 1,
        "share": 0
      },
      {
        "address": "AxFuniPo7RaDgPH6Gizf4GZmLQFc4M5ipckeeZfkrPNn",
        "verified": 1,
        "share": 100
      }
    ],
    "isMutable": true,
    "masterEdition": false
  }
}
```

---

```
GET 
/search?address=EFqtEKp7SNPVYBBXShg6A2jR8xrNnvFypZpTSEEnKD3V HTTP/1.1
```

```json
{
  "mint": "EFqtEKp7SNPVYBBXShg6A2jR8xrNnvFypZpTSEEnKD3V",
  "standard": "metaplex",
  "name": "SOLGods 3846",
  "symbol": "SOLGods",
  "metaplex": {
    "metadataUri": "https://arweave.net/UPAYaK5yh9DyFW_HiL55uVNLF8HYW1621MLKro_Jm64",
    "updateAuthority": "41PLzJby9zqiXjXnY5psHt6zf2X5uaDPiZ5wwRAPKAZM",
    "sellerFeeBasisPoints": 500,
    "primarySaleHappened": 1,
    "owners": [
      {
        "address": "ALNcW6QDNf7H4iNiTM3FD16LZ4zMGyEeCYQiE1AbCoXk",
        "verified": 1,
        "share": 0
      },
      {
        "address": "Em4DcHQwUxhHfEWhz8aZABXU6nUADTGFBPKHoBhKZr9h",
        "verified": 0,
        "share": 100
      }
    ],
    "isMutable": true,
    "masterEdition": false
  }
}
```
