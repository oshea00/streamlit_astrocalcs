import streamlit as st
import astrocalcs
from datetime import date, time, datetime
import openai

st.set_page_config(
    page_title="Astrocalcs - Astronomy Questions",
    page_icon="🌃",
)

# output to sidebar
# st.sidebar.header("Astronomy Questions")

st.title("🌃 Astronomy Questions")

OPENAI = "OPENAI"
openai.api_key = st.secrets[OPENAI]
question = st.text_input("Question",placeholder="Type a question about astronomy",label_visibility="hidden")
if len(question) > 0:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question+"in markdown"+" '{}'",
        max_tokens=1200
    )
    st.write(response.choices[0].text.strip())
