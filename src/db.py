import json
import psycopg2
from psycopg2.extras import DictCursor


class Database:
    def __init__(self, dbname, user, password, host, port):
        self.db = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.db.autocommit = True

    def find(self, address: str) -> dict | None:
        with self.db.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("SELECT * FROM solana WHERE address=%s", (address,))
            item = cursor.fetchone()
            return item[1] if item else None

    def insert(self, address: str, content: dict) -> bool:
        with self.db.cursor(cursor_factory=DictCursor) as cursor:
            try:
                cursor.execute(
                    "INSERT INTO solana VALUES (%s, %s);",
                    (address, json.dumps(content)),
                )
                return True
            except Exception:
                return False
