# Video to Audio Converter

This is a simple GUI-based application to convert video files to audio files. The application is built using Python and Tkinter for the GUI, and it uses MoviePy to handle the video and audio processing.

## Features

- Browse and select a video file (supports various formats like MP4, AVI, etc.)
- Convert the selected video file to an audio file (WAV format)
- Display status updates for the conversion process

## Requirements

- Python 3.x
- tkinter
- moviepy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/video-to-audio-converter.git
    cd video-to-audio-converter
    ```

2. Install the required Python packages:
    ```bash
    pip install moviepy
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Run the application by executing `python app.py`.
2. Click the "Browse" button to select a video file from your computer.
3. Click the "Convert to Audio" button to start the conversion process.
4. The status label will update to show whether the conversion was successful or if there was an error.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [MoviePy](https://zulko.github.io/moviepy/) for the video and audio processing library.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI library.
