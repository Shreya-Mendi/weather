import streamlit as st
from getweather import get_weather,weatherforecast 

st.title("Streamlit Weather App")
st.write("This app shows the script weather conditions at cities.")

city=st.text_input("Enter the name of the city:")

if st.button("Fetch Weather"):
    if city:
        weather, error = get_weather(city)
        if weather:
            st.subheader(f"Weather in {weather['city']}")
            st.write(f"🌡 Temperature: {weather['temp']} °C")
            st.write(f"💧 Humidity: {weather['humidity']}%")
            st.write(f"📖 Description: {weather['description'].capitalize()}")

        else:
            st.error(f"Error: {error}")
    else:
        st.warning("Please enter a city name!")

if st.button("Fetch forecast"):
    df, error = weatherforecast(city)
    if df is not None:
        st.subheader(f"5-day forecast for {city}")
        st.line_chart(df.set_index("datetime")[["temp", "humidity"]])
        
        # to show raw table
        #st.dataframe(df)
    else:
        st.error(f"Error: {error}")    



