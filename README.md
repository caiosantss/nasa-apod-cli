# NASA APOD CLI

#### Video Demo: https://youtu.be/0IqwoNF6KWE

#### Description:

APOD CLI is a command-line application developed as the final project for CS50 Introduction to Python.
The purpose of this project is to provide a simple, accessible, and well-structured way to explore NASA’s Astronomy Picture of the Day (APOD) directly from the terminal.
Instead of relying on a graphical interface or a web browser, this tool allows users to retrieve and interact with scientific astronomy content using a clean command-line experience.

The program uses NASA’s official APOD API to fetch data about daily astronomy images or videos.
When the application is executed, the user can either press Enter to retrieve today’s astronomy picture or provide a specific date in the format YYYY-MM-DD.
For each request, the program displays key information such as the date, title, media type, and a detailed scientific explanation describing the astronomical phenomenon shown.

If the APOD media type is an image, the application automatically downloads and saves the image locally in an organized directory.
If the media type is a video, the program handles this case gracefully by informing the user that downloading is not available and by providing a link to watch the video online.
This behavior ensures that the application remains robust and user-friendly regardless of the type of content returned by the API.

The main logic of the program is implemented in the file `project.py`.
This file contains the `main` function, which is responsible for orchestrating the program’s execution flow, as well as several top-level helper functions.
These functions include input validation, communication with the external NASA API, formatting and displaying information in the terminal, and downloading image files when applicable.
Each function is designed to have a single, clear responsibility, which improves readability, maintainability, and testability.

The file `test_project.py` contains automated unit tests written using pytest.
These tests verify the correct behavior of the program’s core functions, such as date validation and output formatting.
To keep the tests reliable and independent of network conditions, external API calls are not tested directly.
Instead, the tests focus on validating the program’s logic using controlled input data.

The file `requirements.txt` lists all external Python libraries required to run the project.
In this case, the project depends on the `requests` library for making HTTP requests to the NASA API and `pytest` for running automated tests.
All other modules used by the program come from Python’s standard library.

Several design decisions were made during development to keep the project aligned with CS50 requirements.
The application was intentionally implemented without using any web frameworks in order to focus on core Python concepts, such as functions, error handling, file system operations, and testing.
Additionally, the command-line interface was carefully formatted to improve readability and provide a more polished user experience.

Overall, this project demonstrates practical use of Python to solve a real-world problem by integrating an external API, handling errors gracefully, organizing data locally, and writing automated tests.
It reflects a focus on clean code, robustness, and thoughtful software design.
