import streamlit as st
from pytube import YouTube
from pathlib import Path
from utils import get_download_folder, load_css
from downloader import download_youtube_video
import os

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

# YouTube URL to download
youtube_url = st.text_input('Enter the URL of the YouTube video')

# Provide option for users to select download directory or use default
download_option = st.radio(
    "Where would you like to save the video?",
    ('Default download folder', 'Choose a custom folder')
)

if download_option == 'Choose a custom folder':
    custom_folder = st.text_input('Enter the custom folder path')
else:
    custom_folder = None

# Automatically determine the download directory
default_download_directory = get_download_folder()

# Display download button
if st.button('Download Video'):
    if youtube_url:
        if custom_folder:
            download_path = custom_folder
        else:
            download_path = default_download_directory

        with st.spinner('Downloading...'):
            message = download_youtube_video(youtube_url, download_path)
            st.success(message)

        # Display the download link
        video_filename = youtube_url.split('=')[-1] + ".mp4"  # simplified method to create filename
        st.markdown(f"[Download {video_filename}]({os.path.join(download_path, video_filename)})")
    else:
        st.warning("Please enter a YouTube video URL.")
