import streamlit as st
from pytube import YouTube
import os

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

# Streamlit app
st.title('YouTube Video Downloader')

# Input URL from user
youtube_url = st.text_input('Enter the URL of the YouTube video')

# Input directory to save the video
output_directory = st.text_input('Enter the directory to save the video', '.')

if st.button('Download'):
    if youtube_url and output_directory:
        message = download_youtube_video(youtube_url, output_directory)
        st.success(message)
    else:
        st.error('Please provide both a YouTube URL and an output directory.')

# To run this app, save the file and run `streamlit run app.py` in the terminal.
