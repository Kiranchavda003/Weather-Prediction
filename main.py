import streamlit as st
import plotly.express as px
from backend import get_weather_forecast, get_weather_icon

# Add Title, Text Input, Slider, Selectbox, Subheader
st.title("5 Day Weather Forecast")
place = st.text_input("City: ")
days = st.slider("Days", min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select the data to view:",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the Weather Data
    filtered_data = get_weather_forecast(place, days)

    if option == "Temperature":
        temperatures = [day["day"]["avgtemp_c"] for day in filtered_data]
        dates = [day["date"] for day in filtered_data]
        # CREATE A TEMPERATURE PLOT CHART
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        st.write("Weather icons for WeatherAPI:")
        for day in filtered_data:
            if "day" in day and "condition" in day["day"]:
                condition = day["day"]["condition"]["text"]
                icon_path = get_weather_icon(condition)
                if icon_path:
                    st.image(icon_path, caption=condition, width=100)
                else:
                    st.write(f"No icon available for {condition}")
            else:
                st.write("Weather data not available for this day.")
