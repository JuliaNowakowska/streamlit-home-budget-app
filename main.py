import streamlit as st
import sqlite3

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

st.write("""
# Home Budget app
""")

categories = ["food", "flat"]

col1, col2 = st.columns(2)

with col1:
    amount =st.number_input("How much did you spend?", step=0.1)
    shop = st.text_input("Name of the shop:")

with col2:
    category = st.selectbox("Category: ", categories)
    date = st.date_input("When?")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        shop TEXT,
        date TEXT
    )
''')


if st.button('Add'):
    cursor.execute('INSERT INTO expenses (category, amount, shop, date) VALUES (?, ?, ?, ?)', (category, amount, shop, date))
    conn.commit()
    st.success('Expense added successfully!')


# Display expenses
st.header('Expenses this month')
cursor.execute('SELECT * FROM expenses')
expenses = cursor.fetchall()
for expense in expenses:
    st.write(f"category: {expense[0]}, amount: {expense[1]}, shop: {expense[2]}, date: {expense[3]}")