######## CODE STREAMLIT : ########
import streamlit as st
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


def apply_page_config():
    st.set_page_config(
        page_title="Data Reporting Dashboard",
        page_icon="✅",
        layout="wide",
    )


def app_title():
    return st.title("Data Reporting Dashboard")


@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv("data/data.csv", parse_dates=["date"], index_col=[0])


def dates_selection(data):
    st.markdown("Select your date filters")
    col1, col2 = st.columns(2)

    with col1:
        min_date = st.date_input(label="min date", min_value=min(data["date"]), value=(data["date"]).mean(),
                                 max_value=max(data["date"]))

    with col2:
        max_date = st.date_input(label="max date", min_value=min(data["date"]), value=(data["date"]).mean(),
                                 max_value=max(data["date"]))

        return min_date, max_date


def show_data(data, min_date=None, max_date=None):
    st.markdown("### Detailed Data View")
    st.dataframe(data.loc[(data.date >= np.datetime64(min_date)) &
                          (data.date <= np.datetime64(max_date))].head())


if __name__ == '__main__':
    apply_page_config()
    app_title()

    data = get_data()
    min_date, max_date = dates_selection(data)
    show_data(data, min_date, max_date)

######## FIN DU CODE STREAMLIT ########

######## INSEREZ VOS TRAITEMENTS DE DONNEES ET VOS PLOTS ICI : ########

    st.write("Ceci est un exemple")
    fig = plt.figure()

    group_by = data.groupby("satisfaction")["Age"].mean()

    sns.barplot(x=group_by.index, y=group_by.values)
    plt.title("Age moyen par groupes de satisfaction")
    plt.ylabel("Age moyen")
    st.pyplot(fig)


