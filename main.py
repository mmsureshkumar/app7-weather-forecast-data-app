import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next Days")

place = st.text_input(label="Place")

forecast_days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

kind = st.selectbox(label="Select Data to View", options=["Temperature", "Sky"])

st.subheader(f"{kind} for the next {forecast_days} days in {place}")

d, t = get_data(place, forecast_days, kind)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
