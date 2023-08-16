import streamlit as st
import astrocalcs
from datetime import date, time, datetime

st.set_page_config(
    page_title="Astrocalcs - Time",
    page_icon="⏲️",
)

st.title(':timer_clock: Greenwich mean sidereal time (GST)')

c1, c2, c3 = st.columns(3,gap="small")
with c1:
    gyear = st.text_input("Year",str(date.today().year),key="t1")
with c2:
    gmon = st.text_input("Month",str(date.today().month),key="t2")
with c3:
    gday = st.text_input("Day",str(date.today().day),key="t3")

timeLabel = "GMT Time"
strTime = st.text_input(timeLabel,placeholder="Enter time in HH:MM:SS.s",key=timeLabel)

intYear = astrocalcs.getInt(gyear)
intMonth = astrocalcs.getInt(gmon)
intDay = astrocalcs.getInt(gday)

if intYear <= 0:
    st.warning('Year must be positive')
    st.stop()

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
    hour, minute, second = astrocalcs.gmtToGST(intYear,intMonth,intDay,hour,minute,second)
    st.write(f"GST: {int(hour):02}\:{int(minute):02}\:{round(second,2):02}")

