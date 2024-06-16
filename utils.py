import streamlit as st
from pathlib import Path

# Function to determine the default download folder
def get_download_folder():
    return str(Path.home() / "Downloads")

# Function to load custom CSS
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
