import streamlit as st
from pytube import YouTube
from pathlib import Path
from utils import load_css
from downloader import download_youtube_video
import tempfile

# Set the page configuration
st.set_page_config(
    page_title="YouTube Video Downloader", 
    page_icon="static/favicon.ico",
    layout="wide"  # Adjust layout for better responsiveness
)

# Load custom CSS
load_css('css/styles.css')

# Add an icon image
st.image("static/icon.png", width=100)

# Streamlit app
st.title('YouTube Video Downloader')

# YouTube URL to download
youtube_url = st.text_input('Enter the URL of the YouTube video')

# Display download button
if st.button('Download Video'):
    if youtube_url:
        with st.spinner('Downloading...'):
            # Use a temporary directory to save the video
            with tempfile.TemporaryDirectory() as tmpdirname:
                message, video_path = download_youtube_video(youtube_url, tmpdirname)
                st.success(message)

                # Provide a download button for the user to download the file
                if video_path:
                    with open(video_path, 'rb') as file:
                        st.download_button(
                            label='Download Video',
                            data=file,
                            file_name=Path(video_path).name,
                            mime='video/mp4'
                        )
    else:
        st.warning("Please enter a YouTube video URL.")
