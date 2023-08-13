import streamlit as st
import astrocalcs

st.title('Astrocalcs')

m, d = astrocalcs.easter_date(2004)
month = "April" if m == 4 else "March"
st.write(f"Easter Sunday {month} {d}, 2004")
