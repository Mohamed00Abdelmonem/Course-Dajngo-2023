# import requests

# def googleimgdownload(url,savelocation):
  
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(savelocation, 'wb') as file:
#             file.write(response.content)
#         print("Image downloaded successfully.")
#     else:
#         print("Failed to download the image.")


# color_codes = {
#     'red': '\033[91m',
#     'green': '\033[92m',
#     'blue': '\033[94m',
#     'yellow': '\033[93m',
#     'reset': '\033[0m'
# }

# def color_text(text, color):
#     color_code = color_codes.get(color.lower())
#     if color_code:
#         return f"{color_code}{text}{color_codes['reset']}"
#     else:
#         return text

# print(color_text("Hello, world!", "green"))


# from termcolor import colored

# print colored('hello', 'red'), colored('world', 'green')

x = 3
y = 4
z = 5

# print("five") if 3 not in x else print("False")
if any([32 == x, 2 ==y, 1 == z ]):
    print("ok")


def mysum(x,y):
    return x+y
print(mysum(4,3))


print((lambda x,y : x+y) (3,5))
# print(var(-10,2))
    