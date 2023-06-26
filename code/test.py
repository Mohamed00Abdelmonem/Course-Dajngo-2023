# from deepgram import Deepgram
# import asyncio
# import json

# DEEPGRAM_API_KEY = "YOUR_DEEPGRAM_API_KEY"


# async def main():

#     # Initialize the Deepgram SDK
#     deepgram = Deepgram(DEEPGRAM_API_KEY)

#     FILE = 'https://res.cloudinary.com/deepgram/video/upload/v1663090406/dg-audio/Upgrading-phone-plan_pmfsfm.m4a'

#     source = {
#         'url': FILE
#     }

#     response = await asyncio.create_task(
#         deepgram.transcription.prerecorded(
#             source
#         )
#     )

#     print(json.dumps(response, indent=4))

# asyncio.run(main())





# # Define the encoding scheme
# encoding_scheme = {
#     "01": "A",
#     "02": "B",
#     "03": "C",
#     "04": "D",
#     "05": "E",
#     "06": "F",
#     "07": "G",
#     "08": "H",
#     "09": "I",
#     "10": "J",
#     "11": "K",
#     "12": "L",
#     "13": "M",
#     "14": "N",
#     "15": "O",
#     "16": "P",
#     "17": "Q",
#     "18": "R",
#     "19": "S",
#     "20": "T",
#     "21": "U",
#     "22": "V",
#     "23": "W",
#     "24": "X",
#     "25": "Y",
#     "26": "Z",
# }

# # Define the number to be decoded
# encoded_number = "012020101010263101011010000114"

# # Split the encoded number into pairs of digits
# digit_pairs = [encoded_number[i:i+2] for i in range(0, len(encoded_number), 2)]

# # Decode each pair of digits and concatenate the resulting letters
# decoded_message = "".join([encoding_scheme[pair] for pair in digit_pairs])

# print(decoded_message)






# encoded_message = "012020101010263101011010000114"

# # Convert the encoded message to a list of decimal numbers
# encoded_numbers = [int(encoded_message[i:i+2]) for i in range(0, len(encoded_message), 2)]

# # Convert the decimal numbers to their corresponding ASCII characters
# decoded_message = ''.join([chr(num) for num in encoded_numbers])

# print(decoded_message)




    
# n = int(input())
# my_list = [3,4,5,6,2,4,9]
    
# for i in range(n):
#     command = input().split()
        
#     if command[0] == "insert":
#         index = int(command[1])
#         value = int(command[2])
#         my_list.insert(index, value)
#         print(my_list)
#     elif command[0] == "remove":
#             value = command[1]
#             my_list.remove(value)
#     elif command[0] == 'print':
#             print(my_list)        




# my_list = []

#     # read the number of commands
# n = int(input())

#     # process each command
# 4
# for i in range(n):
#         command = input().split()
        
#         # perform the corresponding list operation
#         if command[0] == 'insert':
#             index = int(command[1])
#             value = int(command[2])
#             my_list.insert(index, value)
#         elif command[0] == 'print':
#             print(my_list)
#         elif command[0] == 'remove':
#             value = int(command[1])
#             my_list.remove(value)
#         elif command[0] == 'append':
#             value = int(command[1])
#             my_list.append(value)
#         elif command[0] == 'sort':
#             my_list.sort()
#         elif command[0] == 'pop':
#             my_list.pop()
#         elif command[0] == 'reverse':
#             my_list.reverse()
    
    
    


# def count(n):
        
#         result = ''
#         for i in range(1,n+1):
#             if 1 <= n <= 150:
#                 result+=str(i)
                
#         print(result) 
# count(int(input("enter num:")))        
    



# n = int(input())
# arr = map(int, input().split())
# if 2 <= n and n <= 10:
#         list = list(set(arr))
#         list.sort()
#         print(list[-2])
# n = int(input("num: "))
# arr = input("enter list : ")
# x = arr.split()
# x = set(x)
# x = sorted(x)
# print(x[-2])


# n = int(input("num: "))
# arr = map(int, input().split())
# if 2 <= n and n <= 10:
#     list = list(set(arr))
#     list = sorted(list)
#     print(list[-2])



# n = int(input())
# for i in range(n):
#     print(i*i)



# num = "qA2"
# if 0 <  len(num) < 100:
#     print(str.isalnum(num))
#     print(str.isupper(num))
#     print(str.isalpha(num))
#     print(str.islower(num))
#     print(str.isalnum(num))
#     print(str.isdigit(num))


thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
