import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Weather Forcast Dashboard")
location = st.text_input(label="Location:", placeholder="Type location")
days_slider = st.slider('Forcast Days', max_value=5, min_value=1,help="Slide to select number of days to forecast")
option = st.selectbox("Select Weather Options:",("Temperature","Sky"))

st.subheader(f"{option} for the next {days_slider} days in the {location} area")

dates = ['2025-01-25','2025-01-26','2025-01-27']
temps = [10, 15, 30]

fig = px.line(x=dates, y=temps,labels={'x':'Dates', 'y': 'Temperatures'})
st.plotly_chart(fig)

