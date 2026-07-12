import sqlglot


FORBIDDEN = {
    "DELETE",
    "UPDATE",
    "DROP",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "ATTACH",
    "DETACH",
    "VACUUM",
}


class SQLValidator:

    def __init__(self, schema):
        self.schema = schema

    def validate(self, sql):

        upper = sql.upper()

        for keyword in FORBIDDEN:
            if keyword in upper:
                raise Exception(
                    f"Forbidden SQL detected: {keyword}"
                )

        try:
            sqlglot.parse_one(sql)

        except Exception as e:
            raise Exception(
                f"Invalid SQL: {e}"
            )

        if not upper.strip().startswith("SELECT"):
            raise Exception(
                "Only SELECT statements allowed."
            )

        return True
