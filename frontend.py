import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_api_data

st.title("Weather Forcast Dashboard")
location = st.text_input(label="Location:", placeholder="Type location")
days_slider = st.slider('Forcast Days', max_value=5, min_value=1,help="Slide to select number of days to forecast")
option = st.selectbox("Select Weather Options:",("Temperature","Sky"))

st.subheader(f"{option} for the next {days_slider} days in the {location} area")

if option == "Temperature":
    t, d = get_api_data(location=location,number_of_days=days_slider,option=option)

    fig = px.line(x=d, y=t,labels={'x':'Dates', 'y': 'Temperatures'})
    st.plotly_chart(fig)

