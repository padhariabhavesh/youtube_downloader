import os
import platform
from pathlib import Path
import streamlit as st

def get_download_folder():
    if platform.system() == "Windows":
        return str(Path.home() / "Downloads")
    elif platform.system() == "Darwin":  # macOS
        return str(Path.home() / "Downloads")
    else:
        return str(Path.home() / "Downloads")

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
