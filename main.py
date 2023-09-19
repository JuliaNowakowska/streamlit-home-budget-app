import streamlit as st
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

conn = sqlite3.connect('budget.db')
cursor = conn.cursor()

st.title("Home Budget app")

categories = ["food", "flat"]

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("How much did you spend?", step=0.1)
    shop = st.text_input("Name of the shop:")

with col2:
    category = st.selectbox("Category: ", categories)
    date = st.date_input("When?")
    if st.button('Add'):
        cursor.execute('INSERT INTO expenses (category, amount, shop, date) VALUES (?, ?, ?, ?)',
                       (category, amount, shop, date))
        conn.commit()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        shop TEXT,
        date TEXT
    )
''')

def display_pie_chart(amounts):
    fig1, ax1 = plt.subplots()
    explode = (0.15, 0)
    labels = [f"{category}: {amount}\N{euro sign}" for category, amount in zip(categories, amounts)]
    ax1.pie(amounts, explode=explode, labels=None, shadow=True, startangle=90, colors=['#79155B', '#C23373'],
            autopct=lambda p: '{:.0f}%'.format(p, p * sum(amounts) / 100))
    ax1.legend(labels=labels)
    st.pyplot(fig1)

def display_line_chart(timeline_dictionary):
    if timeline_dictionary is not []:
        x = sorted(timeline_dictionary)
        y = [timeline_dictionary[i] for i in x]
        fig1, ax1 = plt.subplots()
        ax1.plot(x, y)
        plt.xticks(rotation=90)
        st.pyplot(fig1)







# Display expenses
cursor.execute('''SELECT * 
                FROM expenses 
                WHERE category = 'food' ''')
expenses_food = cursor.fetchall()

cursor.execute('''SELECT * 
                    FROM expenses 
                    WHERE category = 'flat' ''')
expenses_flat = cursor.fetchall()

sum_food = sum(expense[2] for expense in expenses_food)
sum_flat = sum(expense[2] for expense in expenses_flat)
amounts = [sum_food, sum_flat]

cursor.execute('''SELECT * 
                    FROM expenses''')
expenses = cursor.fetchall()

timeline_amounts = {}

for expense in expenses:
    if expense[4] not in timeline_amounts.keys():
        timeline_amounts[expense[4]] = expense[2]
    else:
        timeline_amounts[expense[4]] += expense[2]

with col1:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.header('Expenses this month')
    if amounts != [0, 0]:
        display_pie_chart(amounts)
with col2:
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")
    if timeline_amounts:
        display_line_chart(timeline_amounts)



