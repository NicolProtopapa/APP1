#import Streamlit and components 

import streamlit as st 
import time
import requests
from datetime import datetime, timedelta
import pytz

st.sidebar.title("Welcome to our Dashboard Project!")
st.sidebar.write("Contributors: Nikoletta Protopapa, Christos Mattheou")
st.sidebar.write("APIS used : OpenWeatherMap, Unsplash")
st.sidebar.write("Modules used:")
st.sidebar.write("Pytz for worldtime widget")
st.sidebar.write("Time for worldtime and timer")
st.sidebar.write("HTML for static image display")
st.sidebar.write("postimg for picture")



# Get available time zones
timezones = pytz.all_timezones

st.title("Please select a widget from Navigation panel to visit")
# Creating the tabs
tabs = st.tabs(["Home", "Weather", "World Time", "Timer", "Gallery"])

# Content for the "Home" tab
with tabs[0]:
    # Title of the app
    st.write("Online Image Display")
# HTML code to display image hosted on postimg
    html_content = """
<img src="https://i.postimg.cc/fRQy954c/eberhard-grossgasteiger-eo1x-RUAM0-Ok-unsplash.jpg" alt="Mountain Scene">
"""

# Display HTML content
st.markdown(html_content, unsafe_allow_html=True)
# Content for the "Weather Forecast" tab
with tabs[1]:
    # weather forecast
    def get_weather_forecast():

        # Define and pass value for key and city rb
        api_key = "657590925b5cb1b4e04fef3429ba38ce"
        city = "LIMASSOL"
        # OpenWeatherMap 5-day forecast API URL
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        
        # Sending HTTP request
        response = requests.get(url)
        data = response.json()
        
        # Check if the request was successful
        if data.get("cod") != "200":
            st.title("Error:", data.get("message", "Failed to retrieve data"))
            return
        
        # Parsing forecast data
        st.title(f"5-Day Weather Forecast for {city.title()}:\n")
        forecasts = data["list"]
        daily_forecast = {}
        
        # Process data, grouping by day
        for entry in forecasts:
            date_str = entry["dt_txt"].split(" ")[0]
            if date_str not in daily_forecast:
                daily_forecast[date_str] = []
            daily_forecast[date_str].append(entry)
        
        # Displaying forecast for each day
        for date, entries in daily_forecast.items():
            day = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            st.title(f"{day}, {date}:")

            # Daily summary (avg temperature, weather condition)
            temperatures = [entry["main"]["temp"] for entry in entries]
            avg_temp = sum(temperatures) / len(temperatures)
            weather_conditions = [entry["weather"][0]["description"] for entry in entries]
            most_common_weather = max(set(weather_conditions), key=weather_conditions.count)
            
            st.title(f"  Average Temperature: {avg_temp:.2f}°C")
            st.title(f"  Weather: {most_common_weather.capitalize()}")
            st.title("")

    get_weather_forecast()

with tabs [2]: 
        # Streamlit app title
    st.title("WorldTime & Date Widget")
    def clock_App():
    # Dropdown for selecting time zone
       # Get available time zones
        timezones = pytz.all_timezones

        default_timezone = "Asia/Nicosia"

        # Dropdown for selecting time zone
        selected_timezone = st.selectbox("Select a time zone:", timezones, index=timezones.index(default_timezone))

        # Display the current time in the selected time zone
        if True:
            # Get the current time in the selected time zone
            timezone = pytz.timezone(selected_timezone)
            current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

            # Display the current time
            st.subheader(f"Current time in {selected_timezone}:")
            st.write(current_time)

            # Refresh time every second
            
         #   time.sleep(1)
    clock_App()

with tabs[3]:
    # User input for timer duration
    timer_input = st.number_input("Enter countdown time in seconds:", min_value=0, step=1)

    # Start button to initiate countdown
    if st.button("Start Timer"):
        # Create a placeholder to display the countdown
        countdown_display = st.empty()

        # Countdown logic
        for seconds_remaining in range(timer_input, -1, -1):
            # Display the countdown
            countdown_display.markdown(f"<h1 style='text-align: center;'>{seconds_remaining} seconds left</h1>", unsafe_allow_html=True)
            
            # Wait for 1 second
            time.sleep(1)

        # Display message when timer reaches zero
        st.success("Time's up!")
        
# Content for the "Gallery" tab
    with tabs[4]:
    # Random 10 image gallery generator    
        
        UNSPLASH_ACCESS_KEY = "MxrtWqPkYgMvV6KbtkEvxgBk2XVp7Nb-vZv7dsqVHIY"
        UNSPLASH_API_URL = "https://api.unsplash.com/photos/random"

        def fetch_images(count=10):
            """Fetch random images from Unsplash API."""
            response = requests.get(UNSPLASH_API_URL, params={"count": count}, headers={"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"})
            return response.json()

        def main():
            st.title("Automated Image Gallery")
            st.write("This gallery fetches random images from Unsplash.")
            
            # Fetch images
            if st.button("Refresh Images"):
                images = fetch_images(count=10)
            else:
                images = fetch_images(count=10)

            # Display images in a grid format
            cols = st.columns(3)  # Create three columns
            for idx, image in enumerate(images):
                with cols[idx % 3]:  # Cycle through columns
                    st.image(image["urls"]["small"], caption=image["alt_description"], use_column_width=True)

        if __name__ == "__main__":
            main()

   


