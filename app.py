import streamlit as st
from downloader import download_youtube_video
from utils import get_download_folder, load_css

# Set the page configuration
st.set_page_config(page_title="YouTube Video Downloader", page_icon="static/favicon.ico")

# Load custom CSS
load_css('css/styles.css')

# Add an icon image
st.image("static/icon.png", width=100)

# Streamlit app
st.title('YouTube Video Downloader')

# Input URL from user
youtube_url = st.text_input('Enter the URL of the YouTube video')

# Automatically determine the download directory
default_download_directory = get_download_folder()

# Input directory to save the video (pre-filled with default download directory)
output_directory = st.text_input('Enter the directory to save the video', default_download_directory)

if st.button('Download'):
    if youtube_url and output_directory:
        with st.spinner('Downloading...'):
            message = download_youtube_video(youtube_url, output_directory)
            st.success(message)
    else:
        st.error('Please provide both a YouTube URL and an output directory.')
