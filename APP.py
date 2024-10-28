#import Streamlit and components 

import streamlit as st 
import time
import requests
from datetime import datetime, timedelta
import pytz

st.sidebar.title("Welcome to our Dashboard Project!")
st.sidebar.write("Contributors: Nikoletta Protopapa, Christos Mattheou")
st.sidebar.write("APIS used : OpenWeatherMap, Unsplash")
st.sidebar.write("Modules used: Pytz for worldtime widget, Time for worldtime and timer,  HTML for static image display, postimg for picture")

# Get available time zones
timezones = pytz.all_timezones

st.title("Please select a widget from Navigation panel to visit")
# Creating the tabs
tabs = st.tabs(["..", "Weather", "World Time", "Timer", "Gallery"])

# Content for the "Home" tab
with tabs[0]:
    # Title of the app
    st.write("Online Image Display")
# HTML code to display image hosted on postimg
    html_content = """
<img src="https://i.postimg.cc/fRQy954c/eberhard-grossgasteiger-eo1x-RUAM0-Ok-unsplash.jpg" alt="Mountain Scene">
"""