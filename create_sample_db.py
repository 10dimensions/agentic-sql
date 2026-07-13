import sqlite3

conn = sqlite3.connect("sample.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE customers(

id INTEGER PRIMARY KEY,

name TEXT,

country TEXT
)
""")

cur.execute("""
CREATE TABLE orders(

id INTEGER PRIMARY KEY,

customer_id INTEGER,

amount REAL,

created_at TEXT
)
""")

customers = [

(1,"Alice","USA"),

(2,"Bob","USA"),

(3,"Charlie","UK"),

(4,"David","India")

]

orders = [

(1,1,120,None),

(2,1,180,None),

(3,2,50,None),

(4,3,250,None),

(5,4,300,None),

(6,4,450,None)

]

cur.executemany(
    "INSERT INTO customers VALUES(?,?,?)",
    customers
)

cur.executemany(
    "INSERT INTO orders VALUES(?,?,?,?)",
    orders
)

conn.commit()

conn.close()

print("sample.db created.")