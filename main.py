import pandas as pd
import streamlit as st

st.title("Weather Forcast Dashboard")
location = st.text_input(label="Location:", placeholder="Type location")
days_slider = st.slider('Forcast Days', max_value=7, min_value=1,help="Slide to select number of days to forecast")
option = st.selectbox("Select Weather Options:",("Temperature","Sky"))
