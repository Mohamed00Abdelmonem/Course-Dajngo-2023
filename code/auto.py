# from google_images_search import GoogleImagesSearch

# # Initialize the GoogleImagesSearch object
# gis = GoogleImagesSearch('YOUR_API_KEY', 'YOUR_CX')

# # Define the search parameters
# search_params = {
#     'q': 'book',
#     'num': 1,  # Number of images to download
#     'safe': 'high',  # Set the safety level of the search results
#     'fileType': 'jpg',  # Specify the file type of the images
# }

# # Perform the search
# gis.search(search_params)

# # Download the first image
# image = gis.results()[0]
# image.download('img/')  # Provide the desired path to save the image




# import requests

# def download_image(url, save_location):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(save_location, 'wb') as file:
#             file.write(response.content)
#         print("Image downloaded successfully!")
#     else:
#         print("Failed to download the image.")

# # Example usage
# image_url = "https://www.google.com/search?q=book&hl=en&tbm=isch&sxsrf=APwXEddOL3Wfx13yw5-LAwCuyT_QuT5OQQ%3A1686944330948&source=hp&biw=1396&bih=685&ei=SrqMZNyVN7OLkdUPlseh-Ag&iflsig=AOEireoAAAAAZIzIWtCu7mA88fJy2RCdx_NulJRLy94a&ved=0ahUKEwjc4uWsxcj_AhWzRaQEHZZjCI8Q4dUDCAc&uact=5&oq=book&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6BAgjECdQvARYzQlggwxoAXAAeACAAbkCiAHOBpIBBzAuMy4wLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img#imgrc=YlPIoBtDbL_cDM"
# save_path = 'img/'

# download_image(image_url, save_path)







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


