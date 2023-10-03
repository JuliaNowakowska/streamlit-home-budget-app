import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

def display_pie_chart(amounts, categories):
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

        #x = sorted(timeline_dictionary)
        #y = [timeline_dictionary[i] for i in x]

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, color='#79155B')
        plt.xticks(rotation=90)
        ax1.set_ylabel('Summarized expenses (\N{euro sign})')
        ax1.yaxis.grid(which='major', linestyle='--', color='gray', alpha=0.7)
        ax1.plot(x, y, marker='o', linestyle='-', color='#79155B', label='Line Label')
        for i, j in zip(x, y):
            ax1.annotate(str(j), (i, j), textcoords="offset points", xytext=(0, 10), ha='center')
        st.pyplot(fig1)
