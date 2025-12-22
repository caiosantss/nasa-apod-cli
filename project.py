import requests
import datetime
import os

#mypy - type hint checking

def main():
    
    print_header()
    
    try: 
        date = get_date_from_user(
            input("Enter a date (YYYY-MM-DD)(or press Enter for today's date): "))

        #Returns a dictionary with image data != json
        image_data = fetch_nasa_apod(date)
        display_image_info(image_data)
        download_image(image_data, f"./images/apod_{image_data['date']}.jpg")
    except Exception as e:
        print(f"\n{red('ERROR:')} {e}")


def get_date_from_user(date: str) -> str:
    try:
        if not date:
            return datetime.datetime.now().strftime("%Y-%m-%d")

        return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{red('Invalid date format.')} Please use YYYY-MM-DD.")


def fetch_nasa_apod(date: str) -> dict:
    api_key = "DEMO_KEY"  # Replace with your NASA API key
    url = f"https://api.nasa.gov/planetary/apod"
    
    params = {
        "api_key": api_key,
        "date": date
    }
    
    #Validate HTTP request
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data from NASA APOD API: {e}")
    
    #Check for HTTP errors
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from NASA APOD API: {response.status_code} - {response.text}")

    #Return the JSON response as a dictionary
    return response.json()


def display_image_info(image_data: dict) -> None:
    print("\n--- Astronomy Picture Information ---\n")
    print(f" Date        : {image_data['date']}")
    print(f" Title       : {image_data['title']}")
    print(f" Media Type  : {image_data['media_type']}")
    print()
    print(" Description:")
    print(f" {image_data['explanation']}")
    print()
    print(" Image URL:")
    print(f" {image_data.get('hdurl', image_data.get('url', 'N/A'))}")
    print()
    print(f" Copyright   : {image_data.get('copyright', 'Public Domain')}")
    print("-" * 60)

def download_image(image_data: dict, file_path: str) -> None:
    
    if image_data['media_type'] == "video":
        print("\nNote:")
        print(" Today's APOD is a video.")
        print(f" {red('Download is not available for videos.')}")
        print(f" Watch it here: {image_data.get('url')}")
        return
    
    #Check if directory exists, if not create it
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    
    response = requests.get(image_data['url'])
    with open(file_path, "wb") as file:
        file.write(response.content)
        
    print(f"{green('Image downloaded to')} {file_path}")

def print_header():
    print("=" * 60)
    print(" NASA Astronomy Picture of the Day (APOD) CLI ")
    print("=" * 60)
        

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"



if __name__ == "__main__":
    main()