import streamlit as st
import astrocalcs
from datetime import date, time, datetime

st.set_page_config(
    page_title="Astrocalcs - Easter",
    page_icon=":rabbit2:",
)

st.title(":rabbit2: Easter Sunday")

year = st.text_input("Year",placeholder="Enter a year >= 1583")
try:
    if (len(year)>0):
        if int(year)<1583:
            st.warning("Only years >= 1583 will work!")
            st.stop()
        m, d = astrocalcs.easter_date(int(year))
        month = "April" if m == 4 else "March"
        st.write(f"Easter Sunday {month} {d}, {year}")
except:
    st.warning("Only numeric years work!")

with st.expander("See explanation"):
    st.write("Easter day, the date to which such movable feasts as Whitsun and Trinity Sunday "
            "are fixed, is usually the first Sunday after the fourteenth day after the first new Moon after March 21st. "
            "The calculation here devised in 1876 comes from Butcher's Ecclesiastical Calender, "
            "and is valid for all years in the Gregorian calendar from 1583 onwards."
            )
