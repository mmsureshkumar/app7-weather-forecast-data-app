import streamlit as st

st.title("Weather Forecast for Next Days")

strInput = st.text_input(label="Place")

slider = st.slider(label="Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

temp = st.selectbox(label="Select Data to View", options=["Temperature", "Sky"])

st.subheader(f"{temp} for the next {slider} days in {strInput}")
