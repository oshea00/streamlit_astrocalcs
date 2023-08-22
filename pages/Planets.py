import streamlit as st
import astrocalcs
from datetime import date, time, datetime

st.set_page_config(
    page_title="Astrocalcs - Time",
    page_icon=":earth_americas:",
)

st.title(":earth_americas: Planets")

st.markdown("[NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)")