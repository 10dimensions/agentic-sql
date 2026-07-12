class Planner:

    """
    Tiny heuristic planner.

    Picks tables whose names
    appear in the prompt.

    Otherwise returns all tables.
    """

    def select(self, question, schema):

        question = question.lower()

        selected = {}

        for table in schema:

            if table.lower() in question:
                selected[table] = schema[table]

        if selected:
            return selected

        return schema
