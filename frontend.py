import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_api_data

st.title("Weather Forcast Dashboard")
location = st.text_input(label="Location:",key='location')
days_slider = st.slider('Forcast Days', max_value=5, min_value=2,help="Slide to select number of days to forecast")
option = st.selectbox("Select Weather Options:",("Temperature","Overhead Conditions"))

st.subheader(f"{location} Weather: {option} for the next {days_slider} days ")



if location:
    
    working_dataset = get_api_data(location=location,number_of_days=days_slider)
    if option == "Temperature":
        temperature_list = [dict['main']['temp'] for dict in working_dataset]
        date_list = [dict['dt_txt'] for dict in working_dataset]

        fig = px.line(x=date_list, y=temperature_list,labels={'x':'Dates', 'y': 'Temperatures'})
        st.plotly_chart(fig)

    elif option == "Overhead Conditions":
        condition_list = [dict['weather'][0]['main'] for dict in working_dataset]
        date_list = [dict['dt_txt'] for dict in working_dataset]
        image_paths = []
        for condition in condition_list:
            image_paths.append(f'weather_images/{condition}.png')
        print(image_paths)
        st.image(image_paths,width=110)
        st.write(date_list)
        
        description_list = [dict['weather'][0]['description'] for dict in working_dataset]
