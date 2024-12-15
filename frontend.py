import pandas as pd
import streamlit as st
import plotly.express as px
from backend import get_api_data

st.title("Weather Forcast Dashboard")
st.write('By Olwethu Mbane')
st.write('')
content = """
This app provides a 3-hourly weather forecast for up 5-days
"""
st.info(content)

location = st.text_input(label="Location:",key='location').capitalize()
days_slider = st.slider('Forcast Days', max_value=5, min_value=2,help="Slide to select number of days to forecast")
option = st.selectbox("Select Weather Options:",("Temperature","Overhead Conditions"))



if location:
    
    try:
        working_dataset = get_api_data(location=location,number_of_days=days_slider)
        
        st.subheader(f"{location} Weather: {option} for the next {days_slider} days ".title())

        if option == "Temperature":
            temperature_list = [dict['main']['temp']/10 for dict in working_dataset]
            date_list = [dict['dt_txt'] for dict in working_dataset]

            fig = px.line(x=date_list, y=temperature_list,labels={'x':'Dates', 'y': 'Temperatures'})
            st.plotly_chart(fig)

        elif option == "Overhead Conditions":
            condition_list = [dict['weather'][0]['main'] for dict in working_dataset]
            image_paths = []
            for condition in condition_list:
                image_paths.append(f'weather_images/{condition}.png')
            
            st.image(image_paths,width=110,)
           
            
            description_list = [dict['weather'][0]['description'] for dict in working_dataset]
    except KeyError as e:
        st.write(f':red[{location} Does Not Exist as a City or Town in Our Database]')