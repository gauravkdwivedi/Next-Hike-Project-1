import streamlit as st
import numpy as np
import pandas as pd


# Title of the web app
st.title("Telco")

# Load user engagement metrics
engagement_metrics = pd.read_excel('C:/Users/gaura/OneDrive/Visual Studio/NextHike Project 5/user_engagement_metrics.xlsx')

# Load user experience metrics
experience_metrics = pd.read_excel('C:/Users/gaura/OneDrive/Visual Studio/NextHike Project 5/user_experience_metrics.xlsx')

# Load user statisfaction metrics
statisfaction_metrics = pd.read_excel('C:/Users/gaura/OneDrive/Visual Studio/NextHike Project 5/user_statisfaction_metrics.xlsx')

