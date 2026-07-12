import sqlite3


class SchemaReader:

    def __init__(self, db_path):
        self.db = db_path

    def read(self):

        conn = sqlite3.connect(self.db)

        cur = conn.cursor()

        tables = cur.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        ).fetchall()

        schema = {}

        for (table,) in tables:

            cols = cur.execute(
                f"PRAGMA table_info({table})"
            ).fetchall()

            schema[table] = [
                {
                    "name": c[1],
                    "type": c[2]
                }
                for c in cols
            ]

        conn.close()

        return schema
