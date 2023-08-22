import streamlit as st
import astrocalcs
from datetime import date, time, datetime
from math import modf


st.title('📆 Julian Date')

choices = ("Gregorian->Julian","Julian->Gregorian")
with st.sidebar:
  convert = st.radio("Convert",choices)

if convert == choices[0]:
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

if convert == choices[1]:
  julianDate = st.text_input("Julian Date")
  if len(julianDate) > 0:
    julianF = float(julianDate)
    F, I = modf(julianF + .5)
    if I > 2_299_160:
      A = int ((I - 1_867_216.25)/36_524.25)
      B = I + 1 + A - int(A/4)
    else:
      B = I
    C = B + 1524
    D = int((C-122.1)/365.25)
    E = int(365.25*D)
    G = int((C-E)/30.6001)
    dd = C - E + F - int(30.6001*G)
    if G < 13.5:
      m = G - 1
    elif G > 13.5:
      m = G - 13
    if m > 2.5:
      yy = D - 4716
    elif m < 2.5:
      yy = D - 4715

    BCE = ""
    if yy < 0:
      yy = -yy + 1
      BCE = "BCE"

    t, _ = modf(dd)
    hh, mm, ss = astrocalcs.hoursToHMS(t*24)

    dow = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    print(f"Julian {julianF}")
    af, ai = modf((julianF + 1.5)/7)
    print(af)
    day = f"{dow[int(af*7+.5)]}"
    st.write(f"{day}, {int(m):02}/{int(dd):02}/{int(yy):04} {int(hh):02}\:{round(mm+(ss/60)):02} UTC {BCE}")

