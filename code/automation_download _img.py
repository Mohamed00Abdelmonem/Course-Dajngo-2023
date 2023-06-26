
import requests

def download_image(url, save_location):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_location, 'wb') as file:
            file.write(response.content)
        print("Image downloaded successfully!")
    else:
        print("Failed to download the image.")

# Example usage
image_url = "https://www.shutterstock.com/image-illustration/military-robot-destroyed-city-future-apocalypse-1207217143"
save_path = 'img/img.jpg'

download_image(image_url,save_path)

