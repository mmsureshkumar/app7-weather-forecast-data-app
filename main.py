import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next Days")

place = st.text_input(label="Place")

forecast_days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

kind = st.selectbox(label="Select Data to View", options=["Temperature", "Sky"])

st.subheader(f"{kind} for the next {forecast_days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, forecast_days)
        match kind:
            case "Temperature":
                temperature = [dict['main']['temp']/10 for dict in filtered_data]
                dates = [dict['dt_txt'] for dict in filtered_data]
                figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature"})
                st.plotly_chart(figure)
            case "Sky":
                images = {'Clear' : 'images/clear.png', 'Clouds' : 'images/cloud.png', 'Rain' : 'images/rain.png', 'Snow' : 'images/snow.png'}
                sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
                print(sky_conditions)
                imagepaths = [images[x] for x in sky_conditions]
                st.image(imagepaths, width=100)
    except:
            st.text("Place you entered is not exist. Kindly re-enter the place that exist")
