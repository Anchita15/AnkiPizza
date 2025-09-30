import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AnkiPizza", page_icon="🍕", layout="wide")

# Your GitHub Pages URL (works after you enable Pages on the repo)
PAGES_URL = "https://anchita15.github.io/AnkiPizza/"

# Make Streamlit container full width
st.markdown("""
<style>
  .stApp > header, .stApp > footer {visibility: hidden;}
  .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
  iframe {width: 100% !important; border: 0;}
</style>
""", unsafe_allow_html=True)

st.markdown("### 🍕 AnkiPizza")


# Load your site directly. Adjust height if you need more/less.
components.iframe(PAGES_URL, height=1800, scrolling=True)
