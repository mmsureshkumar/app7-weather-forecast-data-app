import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Next Days")

strInput = st.text_input(label="Place")

days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

temp = st.selectbox(label="Select Data to View", options=["Temperature", "Sky"])

st.subheader(f"{temp} for the next {days} days in {strInput}")


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperature = [11, 12, 15]
    temperature = [days * i for i in temperature]
    return dates, temperature


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
