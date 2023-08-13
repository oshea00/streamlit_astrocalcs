import streamlit as st
import astrocalcs
from datetime import date, time

st.title('Astrocalcs')

easter, julian = st.tabs(["Easter Sunday","Julian Dates"])

with easter:
  year = st.number_input("Year",1583)
  m, d = astrocalcs.easter_date(year)
  month = "April" if m == 4 else "March"
  st.write(f"Easter Sunday {month} {d}, {year}")

with julian:
  gdate = st.date_input("Date",date.today(),date(1582,10,15),format="MM/DD/YYYY")
  gtime = st.time_input("Time UTC",value=time(0,0),step=300)
  julian = astrocalcs.julianDate(gdate.year,gdate.month,gdate.day,gtime.hour,gtime.minute,gtime.second)
  mjd = astrocalcs.modifiedJulianDate(gdate.year,gdate.month,gdate.day,gtime.hour,gtime.minute,gtime.second)
  st.write(f"Julian date {julian}")
  st.write(f"Modified Julian date (MJD) {mjd}")

