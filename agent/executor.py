import sqlite3


class SQLExecutor:

    def __init__(self, db_path):
        self.db = db_path

    def execute(self, sql):

        conn = sqlite3.connect(self.db)

        conn.row_factory = sqlite3.Row

        cur = conn.cursor()

        cur.execute(sql)

        rows = cur.fetchall()

        conn.close()

        return [
            dict(r)
            for r in rows
        ]
