import sqlite3

conn = sqlite3.connect('menu.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS menu (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Foodname TEXT NOT NULL,
    Quantity INTEGER NOT NULL,
    TotalPrice REAL NOT NULL
)
''')

'''menu_items = [('Burger', 5.99),
    ('Pizza', 8.99),
    ('Pasta', 7.49),
    ('Fries', 2.99)
]

cursor.executemany('INSERT INTO menu (name, price) VALUES (?, ?)', menu_items)'''
conn.commit()
conn.close()