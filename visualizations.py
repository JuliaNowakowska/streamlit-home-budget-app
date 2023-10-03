import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

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
        x = sorted(timeline_dictionary)
        y = [timeline_dictionary[i] for i in x]

        fig1, ax1 = plt.subplots()
        ax1.plot(x, y, color='#79155B')
        plt.xticks(rotation=90)
        ax1.set_ylabel('Summarized expenses (\N{euro sign})')
        ax1.yaxis.grid(which='major', linestyle='--', color='gray', alpha=0.7)
        ax1.plot(x, y, marker='o', linestyle='-', color='#79155B', label='Line Label')
        for i, j in zip(x, y):
            ax1.annotate(str(j), (i, j), textcoords="offset points", xytext=(0, 10), ha='center')

        st.pyplot(fig1)
