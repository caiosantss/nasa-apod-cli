import requests
import datetime

#mypy - type hint checking
#import argparse - command line argument parsing - help tool


def main():
    
    print("NASA Astronomy Picture of the Day Downloader")
    
    date = get_date_from_user(
        input("Enter a date (YYYY-MM-DD)(or press Enter for today's date): ")
    )

    #Returns a dictionary with image data != json
    image_data = fetch_nasa_apod(date)
    display_image_info(image_data)
    download_image(image_data, f"./images/apod_{image_data['date']}.jpg")


def get_date_from_user(date: str) -> str:
    try:
        if not date:
            return datetime.datetime.now().strftime("%Y-%m-%d")

        return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")


def fetch_nasa_apod(date: str) -> dict:
    api_key = "DEMO_KEY"  # Replace with your NASA API key
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"
    try:
        return requests.get(url).json()
    except requests.RequestException as e:
        raise SystemExit(f"Error fetching data from NASA APOD API: {e}")



def display_image_info(image_data: dict) -> None:
    print(f"Date: {image_data['date']}")
    print(f"Title: {image_data['title']}")
    print(f"Explanation: {image_data['explanation']}")
    #If its an video, don't have hdurl, SO DE DEFAULT value is url
    print(f"URL: {image_data.get('hdurl', image_data.get('url', 'N/A'))}")
    # Not all contents have copyright - use get with a default value
    print(f"Copyright: {image_data.get('copyright', 'Public Domain')}")


def download_image(image_data: dict, file_path: str) -> None:
    if image_data['media_type'] == "video":
        print("As the media type is a video it will not be dowloaded")
    else:
        response = requests.get(image_data['url'])
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        print(f"Image downloaded to {file_path}")
        


if __name__ == "__main__":
    main()