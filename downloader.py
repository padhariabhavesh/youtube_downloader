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

        # Get the filename of the downloaded video
        filename = os.path.basename(stream.default_filename)

        return f"Video downloaded successfully. You can find it in your device's download folder as '{filename}'."
    except Exception as e:
        return f"An error occurred: {e}"
