import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from datetime import datetime

def display_pie_filter(expenses, filter):
    if filter == "" or filter == "All time":
        sum_expenses_food = sum(expense[2] for expense in expenses if expense[1] == 'food')
        sum_expenses_flat = sum(expense[2] for expense in expenses if expense[1] == 'flat')
    else:
        sum_expenses_food = sum(expense[2] for expense in expenses if expense[1] == 'food' and expense[4][:7] == filter)
        sum_expenses_flat = sum(expense[2] for expense in expenses if expense[1] == 'flat' and expense[4][:7] == filter)
    amounts = [sum_expenses_food, sum_expenses_flat]
    categories = ["food", "flat"]
    fig1, ax1 = plt.subplots()
    explode = (0.15, 0)
    labels = [f"{category}: {amount}\N{euro sign}" for category, amount in zip(categories, amounts)]
    ax1.pie(amounts, explode=explode, labels=None, shadow=True, startangle=90, colors=['#79155B', '#C23373'],
            autopct=lambda p: '{:.0f}%'.format(p, p * sum(amounts) / 100))
    ax1.legend(labels=labels)
    st.pyplot(fig1)


def display_line_chart(timeline_dictionary):
    if timeline_dictionary is not []:
        dates = [datetime.strptime(date, "%Y-%m-%d") for date in timeline_dictionary.keys()]
        # Group data by month and calculate the sum of expenses for each month
        monthly_summary = {}
        for date, expense in zip(dates, timeline_dictionary.values()):
            month_year = date.strftime("%b %Y")
            if month_year not in monthly_summary:
                monthly_summary[month_year] = 0
            monthly_summary[month_year] += expense

        # Extract sorted month-year labels and corresponding sums
        # Sort the month-year labels in chronological order
        sorted_months = sorted(monthly_summary.keys(), key=lambda x: datetime.strptime(x, "%b %Y"))

        # Extract sorted month-year labels and corresponding sums
        x = sorted_months
        y = [monthly_summary[i] for i in x]

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, color='#79155B')
        plt.xticks(rotation=90)
        ax1.set_ylabel('Summarized expenses (\N{euro sign})')
        ax1.set_ylim(0,max(y)+50)
        ax1.yaxis.grid(which='major', linestyle='--', color='gray', alpha=0.7)
        ax1.plot(x, y, marker='o', linestyle='-', color='#79155B', label='Line Label')
        for i, j in zip(x, y):
            ax1.annotate(str(j), (i, j), textcoords="offset points", xytext=(0, 10), ha='center')
        st.pyplot(fig1)

def bar_plot_shops(expenses):
    shops = [expense[3] for expense in expenses]
    shops = list(set(shops))
    months = [expense[4][:7] for expense in expenses if expense[4][:7]]
    months = sorted(list(set(months)))

    monthly_summary = {}

    for month in months:
        monthly_summary[month] = []
        for shop in shops:
            amount = sum(expense[2] for expense in expenses if expense[3] == shop and expense[4][:7] == month)
            monthly_summary[month].append(amount)

    shop_all_values = {}
    for i in range(len(shops)):
        shop_all_values[shops[i]] = []
        for val in monthly_summary.values():
            shop_all_values[shops[i]].append(val[i])
        shop_all_values[shops[i]] = tuple(shop_all_values[shops[i]])

    x = np.arange(len(months))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in shop_all_values.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Amount of money (euro)')
    ax.set_title('Expenses by shops')
    ax.set_xticks(x + width, months)
    plt.xticks(rotation=90)
    ax.legend(loc='upper left')
    ax.set_ylim(0, 250)
    st.pyplot(fig)
