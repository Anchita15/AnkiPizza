import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AnkiPizza", page_icon="🍕", layout="wide")

PAGES_URL = "https://anchita15.github.io/AnkiPizza/"

# Remove Streamlit chrome *completely* (use display:none so nothing overlays/crops)
st.markdown("""
<style>
  header[data-testid="stHeader"] { display: none; }   /* remove top bar */
  footer { display: none; }                           /* remove footer */
  .block-container { padding:0 !important; margin:0 !important; max-width:100% !important; }
  iframe { width:100% !important; border:0; }
</style>
""", unsafe_allow_html=True)

# Big enough height; increase if you need more page
components.iframe(PAGES_URL, height=2000, scrolling=True)
