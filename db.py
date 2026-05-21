import sqlite3

def to_connect():
    conn = sqlite3.connect("store.db")
    return conn

def create_table_products():
    conn = to_connect()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """
    )
    conn.commit()
    conn.close()

def add_product(name, price):
    conn = to_connect()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO products (name, price)
            VALUES (?, ?)
        """, (name, price)
    )

    conn.commit()
    conn.close()

def read_products():
    conn = to_connect()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT id, name, price FROM products
        """
    )
    products = cursor.fetchall()
    for product in products:
        print(product)

create_table_products()

add_product('Havaianas flip-flops', 39.99)
add_product('Oxford Tulip Ceramic Mug (330ml)', 19.99)
add_product('Bicycle Standard Playing Cards', 39.90)

read_products()