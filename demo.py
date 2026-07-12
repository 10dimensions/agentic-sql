from agent.schema import SchemaReader
from agent.planner import Planner
from agent.llm import OllamaLLM
from agent.validator import SQLValidator
from agent.executor import SQLExecutor

DB_PATH = "sample.db"
MODEL = "qwen3"


def main():

    question = input("\nAsk a question: ")

    schema = SchemaReader(DB_PATH).read()

    planner = Planner()

    relevant_schema = planner.select(question, schema)

    llm = OllamaLLM(MODEL)

    sql = llm.generate_sql(
        question,
        relevant_schema
    )

    print("\nGenerated SQL\n")
    print(sql)

    validator = SQLValidator(schema)

    validator.validate(sql)

    executor = SQLExecutor(DB_PATH)

    rows = executor.execute(sql)

    print("\nResult\n")

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
