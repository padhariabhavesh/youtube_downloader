# Youtube Downloader
This project is a web application that allows users to download YouTube videos by providing a URL. 
# YouTube Video Downloader

A simple web application built with Streamlit that allows users to download YouTube videos. The app provides a user-friendly interface where users can enter the URL of a YouTube video and download it to their local device.

## Features

- Download YouTube videos in the highest available resolution.
- Simple and responsive user interface.
- Supports downloading directly to the user's device.
- Custom CSS for styling the application.

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Clone the Repository


```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
```

# Install Dependencies
```
pip install -r requirements.txt
```

# Usage

To run the application, navigate to the project directory and execute the following command:
```
streamlit run app.py

```
This will start the Streamlit server and open the application in your default web browser. You can also access the app by navigating to http://localhost:8501 in your browser.

# Downloading a Video

Enter the URL of the YouTube video you want to download.
Click the "Download Video" button.
The app will process the request and provide a download button for the video file.

# Project Structure
```
youtube-video-downloader/
│
├── app.py                  # Main application script
├── downloader.py           # Script containing the video downloading logic
├── utils.py                # Utility functions for the application
├── requirements.txt        # List of dependencies
├── css/
│   └── styles.css          # Custom CSS for styling the app
├── static/
│   ├── favicon.ico         # Favicon for the app
│   └── icon.png            # Icon image displayed in the app
└── README.md               # Project documentation
```
Code Overview
app.py

The main application script that sets up the Streamlit app. It includes:

    Page configuration and custom CSS loading.
    Input field for the YouTube video URL.
    Logic to handle video downloading and provide a download button for the user.

downloader.py

Contains the download_youtube_video function which:

    Creates a YouTube object using the provided URL.
    Fetches the highest resolution stream available.
    Downloads the video to the specified output path.

utils.py

Utility functions used in the application:

    load_css(file_path): Loads custom CSS from a file.
    get_download_folder(): Determines the default download folder (not used in the final implementation but kept for potential future use).

Dependencies

    streamlit: For building the web interface.
    pytube: For downloading YouTube videos.

These can be installed via pip using the requirements.txt file.
Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements

    Streamlit for providing an easy-to-use framework for building web applications.
    PyTube for enabling YouTube video downloading functionality.

Feel free to customize this README.md to better fit your project's needs.


This `README.md` provides a comprehensive overview of the project, including installation instructions, usage guide, project structure, and code overview. It also includes sections for contributing and licensing. Adjust the content as necessary to match your specific project details.

