import streamlit as st
import astrocalcs
from datetime import date, time
import re

def getInt(s):
  i = 0
  match = re.search("\-{0,1}[\d]+",s)
  if match:
    i = int(match[0])
  return i

st.title('Astrocalcs')

easter, julian = st.tabs(["Easter Sunday","Julian Dates"])

with easter:
  year = st.number_input("Year",1583)
  m, d = astrocalcs.easter_date(year)
  month = "April" if m == 4 else "March"
  st.write(f"Easter Sunday {month} {d}, {year}")
  with st.expander("See explanation"):
    st.write("Easter day, the date to which such movable feasts as Whitsun and Trinity Sunday "
             "are fixed, is usually the first Sunday after the fourteenth day after the first new Moon after March 21st. "
             "The calculation here devised in 1876 comes from Butcher's Ecclesiastical Calender, "
             "and is valid for all years in the Gregorian calendar from 1583 onwards."
             )

with julian:
  c1, c2, c3 = st.columns(3,gap="small")
  with c1:
    gyear = st.text_input("Year",str(date.today().year))
  with c2:
    gmon = st.text_input("Month",str(date.today().month))
  with c3:
    gday = st.text_input("Day",str(date.today().day))
  isBce = st.checkbox("Is BCE")
  gtime = st.time_input("Time UTC",value=time(0,0),step=300)

  intYear = getInt(gyear)
  intMonth = getInt(gmon)
  intDay = getInt(gday)
  
  if intYear <= 0:
    st.warning('Year must be positive')
    st.stop()

  if isBce:
    intYear = -(intYear-1)

  if intYear < -4712:
    st.warning('Year cannot be before 4713 BCE')
    st.stop()


  julian = astrocalcs.julianDate(intYear,intMonth,intDay,gtime.hour,gtime.minute,gtime.second)
  mjd = astrocalcs.modifiedJulianDate(intYear,intMonth,intDay,gtime.hour,gtime.minute,gtime.second)
  st.write(f"Julian date {julian}")
  st.write(f"Modified Julian date (MJD) {mjd}")

