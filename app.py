######## CODE STREAMLIT : ########
import streamlit as st
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Data Reporting Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Data Reporting Dashboard")

@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv("data/data.csv", parse_dates=["date"], index_col=[0])

data = get_data()

st.markdown("Select your date filters")


col1, col2 = st.columns(2)

with col1:
    min_date = st.date_input(label="min date", min_value=min(data["date"]), value= (data["date"]).mean(),
                  max_value=max(data["date"]))

with col2:
    max_date = st.date_input(label="max date", min_value=min(data["date"]), value= (data["date"]).mean(),
                  max_value=max(data["date"]))


st.markdown("### Detailed Data View")
st.dataframe(data.loc[(data.date >= np.datetime64(min_date))  &
             (data.date <= np.datetime64(max_date))].head())


######## FIN DU CODE STREAMLIT ########

######## INSEREZ VOS TRAITEMENTS DE DONNEES ET VOS PLOTS ICI : ########

fig = plt.figure()

group_by = data.groupby("satisfaction")["Age"].mean()

sns.barplot(x = group_by.index, y = group_by.values)