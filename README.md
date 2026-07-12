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
