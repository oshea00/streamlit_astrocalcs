import streamlit as st
import astrocalcs
from datetime import date, time, datetime
import openai

OPENAI = "OPENAI"
openai.api_key = st.secrets[OPENAI]

st.set_page_config(
    page_title="Astrocalcs",
    page_icon=":star2:",
)

st.title(':star2: - Astrocalcs')

introMd = """
### An Assembly of Astronomical Calculations 

You'll find some useful astronomical calculations here and a place to ask astronomy questions.

Have Fun!

"""

st.markdown(introMd)