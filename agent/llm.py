import ollama

from agent.prompts import SYSTEM_PROMPT


class OllamaLLM:

    def __init__(self, model="qwen3"):
        self.model = model

    def _schema_to_text(self, schema):

        lines = []

        for table, cols in schema.items():

            lines.append(f"\nTable: {table}")

            for col in cols:
                lines.append(
                    f"  - {col['name']} ({col['type']})"
                )

        return "\n".join(lines)

    def generate_sql(self, question, schema):

        schema_text = self._schema_to_text(schema)

        prompt = f"""
Database schema

{schema_text}

Question

{question}

Return SQL only.
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        sql = response["message"]["content"]

        sql = sql.replace("```sql", "")
        sql = sql.replace("```", "")

        return sql.strip()
