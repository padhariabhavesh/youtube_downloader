import os
from pytube import YouTube

# Function to download YouTube video
def download_youtube_video(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=output_path)

        # Get the full path of the downloaded video
        video_path = os.path.join(output_path, stream.default_filename)

        return f"Video downloaded successfully. You can find it in '{output_path}' as '{stream.default_filename}'.", video_path
    except Exception as e:
        return f"An error occurred: {e}", None
