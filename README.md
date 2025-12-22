# NASA APOD CLI

#### Video Demo:  https://youtu.be/0IqwoNF6KWE

#### Description:
NASA APOD CLI is a command-line application developed as the final project for CS50 Introduction to Python.

The program uses NASA’s official Astronomy Picture of the Day (APOD) API to
retrieve and display daily astronomy images and scientific explanations directly in the terminal.

Users can optionally enter a specific date or press Enter to retrieve today’s
astronomy picture. The application displays the image’s title, date, explanation, media type, and source URL in a well-formatted CLI interface.

If the APOD media type is an image, the program automatically downloads and saves the file locally. If the media type is a video, the program informs the user and provides a link to watch it online.

The project demonstrates the use of external APIs, error handling, date
validation, file system operations, and automated testing using pytest, all
implemented in Python without any web frameworks.