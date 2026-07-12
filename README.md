```
Instructions:

1) python create_sample_db.py
2) ollama pull qwen3
3) python demo.py

Example:
Ask a question:
Top customers by total spending

Generated SQL:
SELECT
    customers.name,
    SUM(orders.amount) AS total_spending
FROM customers
JOIN orders
ON customers.id = orders.customer_id
GROUP BY customers.id
ORDER BY total_spending DESC;

Output:
{'name': 'David', 'total_spending': 750.0}
{'name': 'Charlie', 'total_spending': 250.0}
{'name': 'Alice', 'total_spending': 300.0}
{'name': 'Bob', 'total_spending': 50.0}
```

```
Improvements:
Schema-aware validation: Parse the SQL AST with sqlglot and verify every referenced table and column exists in the discovered schema instead of only checking syntax.
Retry loop: If execution fails, send the error message (not the query results) back to the LLM and ask it to generate corrected SQL, limiting retries to 2–3 attempts.
Relationship discovery: Read foreign keys using PRAGMA foreign_key_list(table) so the prompt includes table relationships and the model can produce more accurate joins.
Better table selection: Replace the simple keyword heuristic with embeddings (e.g., sentence-transformers) so only the most relevant tables are included in the prompt for larger schemas.
Conversation context: Maintain a short history so follow-up questions like "Now only for India" can reuse the previous query context.
Optional result summarization: Add a second LLM call that summarizes the returned rows. Keep it configurable so privacy-sensitive deployments can disable sending result data to the model.
Configuration: Move the database path, model name, and retry settings into a small configuration file or environment variables.
Logging: Record the user prompt, generated SQL, validation outcome, and execution time for debugging and auditing.
```
