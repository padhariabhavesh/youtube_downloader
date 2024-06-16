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

        return f"Video downloaded successfully and saved to {output_path}"
    except Exception as e:
        return f"An error occurred: {e}"
