import streamlit as st
import astrocalcs
from datetime import date, time, datetime


st.title('📆 Julian Date')

c1, c2, c3 = st.columns(3,gap="small")
with c1:
  gyear = st.text_input("Year",str(date.today().year))
with c2:
  gmon = st.text_input("Month",str(date.today().month))
with c3:
  gday = st.text_input("Day",str(date.today().day))
isBce = st.checkbox("Is BCE")
gtime = st.time_input("Time UTC",value=time(0,0),step=900)

intYear = astrocalcs.getInt(gyear)
intMonth = astrocalcs.getInt(gmon)
intDay = astrocalcs.getInt(gday)

if intYear <= 0:
  st.warning('Year must be positive')
  st.stop()

if isBce:
  intYear = -(intYear-1)

if intYear < -4712:
  st.warning('Year cannot be before 4713 BCE')
  st.stop()

if intMonth < 1 or intMonth > 13:
  st.warning('Month must be 1-12')
  st.stop()

if intDay < 1 or intMonth > 31:
  st.warning('Day must be 1-31')
  st.stop()

julian = astrocalcs.julianDate(intYear,intMonth,intDay,gtime.hour,gtime.minute,gtime.second)
mjd = astrocalcs.modifiedJulianDate(intYear,intMonth,intDay,gtime.hour,gtime.minute,gtime.second)
st.write(f"Julian date {julian}")
st.write(f"Modified Julian date (MJD) {mjd}")

