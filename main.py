import streamlit as st
import sqlite3
from database import create_expense, fetch_expenses, initialize_database
from visualizations import display_pie_chart, display_line_chart, display_pie_filter

categories = ["food", "flat"]

def main():
    conn, cursor = initialize_database()

    st.set_page_config(layout="wide")
    st.title("Home Budget app")

    col1, col2 = st.columns(2)

    with col1:
        amount = st.number_input("How much did you spend?", step=0.1)
        shop = st.text_input("Name of the shop:")

    with col2:
        category = st.selectbox("Category: ", categories)
        date = st.date_input("When?")
        if st.button('Add'):
            create_expense(cursor, conn, category, amount, shop, date)



    expenses_food = fetch_expenses(cursor, 'food')
    expenses_flat = fetch_expenses(cursor, 'flat')

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
        st.header('Expenses')
        date_filter = st.selectbox("", ["All time", "Jan 2023", "Feb 2023"])
        if date_filter:
            display_pie_filter(expenses, date_filter)
        if amounts != [0, 0]:
            display_pie_chart(amounts, categories)
    with col2:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        if timeline_amounts:
            display_line_chart(timeline_amounts)



if __name__ == "__main__":
    main()