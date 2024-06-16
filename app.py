import streamlit as st
from pytube import YouTube
from pathlib import Path
from utils import get_download_folder, load_css
from downloader import download_youtube_video

# Function to download YouTube video
def download_youtube_video(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=output_path)

        return f"Video downloaded successfully and saved to {output_path}"
    except Exception as e:
        return f"An error occurred: {e}"

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

# YouTube URL to download (hardcoded for demonstration purposes)
youtube_url = st.text_input('Enter the URL of the YouTube video')

# Automatically determine the download directory
default_download_directory = get_download_folder()

# Display download button
if st.button('Download Video'):
    if youtube_url:
        with st.spinner('Downloading...'):
            message = download_youtube_video(youtube_url, default_download_directory)
            st.success(message)
    else:
        st.warning("Please enter a YouTube video URL.")
