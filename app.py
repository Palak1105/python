import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
        df = read_csv=("data.csv",index_col = 0)
        return df


st.title("AIR QUALITY ANALYSIS")

st.sidebar.header("Project Options")

options=['Agencies',
        ' Types of Areas',
        'Date vs so2',
        'State vs so2',
        'State vs no2',
        'State vs rspm',
        'State vs spm ',
        'State vs pm2_5']

choice = st.sidebar.selectbox(" select an option",options)

df = load_data()