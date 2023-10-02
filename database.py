import sqlite3

def initialize_database():
    conn = sqlite3.connect('budget.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            category TEXT,
            amount REAL,
            shop TEXT,
            date TEXT)''')

    return conn, cursor


def create_expense(cursor, conn, category, amount, shop, date):
    cursor.execute('INSERT INTO expenses (category, amount, shop, date) VALUES (?, ?, ?, ?)',
                   (category, amount, shop, date))
    conn.commit()

def fetch_expenses(cursor, category):
    cursor.execute('SELECT * FROM expenses WHERE category = ?', (category,))
    return cursor.fetchall()