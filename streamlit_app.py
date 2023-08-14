import streamlit as st
import astrocalcs
from datetime import date, time, datetime
import openai

OPENAI = "OPENAI"
openai.api_key = st.secrets[OPENAI]

st.title('Astrocalcs')

easter, julian, timeref, astroquery = st.tabs(["Easter Sunday","Julian Dates","Time","Astronomy Questions"])

with easter:
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

with julian:
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

with timeref:
  
  gmtOption = 'Greenwich mean time (GMT) to Greenwich mean sidereal time (GST)'
  localOption = 'Local time to Local mean sidereal time (LST)'

  option = st.selectbox('Conversions',
                        (gmtOption,
                         localOption))

  c1, c2, c3 = st.columns(3,gap="small")
  with c1:
    gyear = st.text_input("Year",str(date.today().year),key="t1")
  with c2:
    gmon = st.text_input("Month",str(date.today().month),key="t2")
  with c3:
    gday = st.text_input("Day",str(date.today().day),key="t3")
  isBce = st.checkbox("Is BCE",key="t4")

  timeLabel = "GMT Time" if option == gmtOption else "Local Time"
  if option == gmtOption:
      strTime = st.text_input(timeLabel,placeholder="HH:MM:SS.s",key=timeLabel)
  else:
      strTime = st.text_input(timeLabel,placeholder="HH:MM:SS.s",key=timeLabel,
                              value=f"{datetime.now().hour:02}:{datetime.now().minute:02}:{datetime.now().second:02}")

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

  hour, minute, second, isValid = astrocalcs.getTime(strTime)

  if isValid:
    if option == gmtOption:
      hour, minute, second = astrocalcs.gmtToGST(intYear,intMonth,intDay,hour,minute,second)
      st.write(f"GST: {int(hour):02}\:{int(minute):02}\:{round(second,2):02}")
    else:
      st.write(f"LST: In-Work")
  else:
    st.warning('Invalid time')

with astroquery:
  question = st.text_input("Question",placeholder="Type a question about astronomy")
  if len(question) > 0:
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=question+" '{}'",
      max_tokens=1200
    )
    st.write(response.choices[0].text.strip())
