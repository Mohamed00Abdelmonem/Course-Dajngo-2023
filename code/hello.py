
# for loop

# x = int(input("enter row: "))
# for i in range(1,x+1):
#     print("*" * i)


# oop

# class Calc:
#     def sum (self,x,y):
#         return x+y
#     def mult (self,x,y):
#         return x*y
#     def div (self,x,y):
#         return x/y
#     def power (self,x,y):
#         return x**y
    
# oper = Calc()
# print(oper.div(40,5))    


# class Calc:
#     def summ (self,x,y):
#         return x+y
#     def mult (self,x,y):
#         return x*y
#     def __init__(self,name):
#        print(f"Welcome {name}")
  

# class SicCalc(Calc):
#     def div(self,x,y):
#         return x/y
#     def power (self,x,y):
#         return x**y
#     # error ف هيطلع ليا method تانيه Class كدا انا اخذت من       
#     # Class Calc  ف المفروض اخد وراثه من 
# oper = SicCalc('mohamed')    
# print(oper.summ(3,4))
# print(oper.mult(3,4))
# print(oper.div(3,4))
# print(oper.power(3,4))






# class A:

#      def do(self):
#         print("in A")
        
# class B(A):
#    pass
        
# class C:
#      def do(self):
#         print("in V")
        
# class D(B,C):
#     pass

        
# object_1 = D()
# object_1.do()
# # (MRO)Method Resolution Order
# print(D.mro())     







# # importing google_images_download module
# from google_images_download import google_images_download

# # creating object
# response = google_images_download.googleimagesdownload()

# search_queries =
# [
	
# 'The smartphone also features an in display fingerprint sensor.',
# 'The pop up selfie camera is placed aligning with the rear cameras.',
# '''In terms of storage Vivo V15 Pro could offer
# up to 6GB of RAM and 128GB of onboard storage.''',
# 'The smartphone could be fuelled by a 3 700mAh battery.',
# ]


# def downloadimages(query):
# 	# keywords is the search query
# 	# format is the image file format
# 	# limit is the number of images to be downloaded
# 	# print urls is to print the image file url
# 	# size is the image size which can
# 	# be specified manually ("large, medium, icon")
# 	# aspect ratio denotes the height width ratio
# 	# of images to download. ("tall, square, wide, panoramic")
# 	arguments = {"keywords": query,
# 				"format": "jpg",
# 				"limit":4,
# 				"print_urls":True,
# 				"size": "medium",
# 				"aspect_ratio":"panoramic"}
# 	try:
# 		response.download(arguments)
	
# 	# Handling File NotFound Error
# 	except FileNotFoundError:
# 		arguments = {"keywords": query,
# 					"format": "jpg",
# 					"limit":4,
# 					"print_urls":True,
# 					"size": "medium"}
					
# 		# Providing arguments for the searched query
# 		try:
# 			# Downloading the photos based
# 			# on the given arguments
# 			response.download(arguments)
# 		except:
# 			pass

# # Driver Code
# for query in search_queries:
# 	downloadimages(query)
# 	print()











# oop 2 


'''
Bank

  - create clinet (name , age )
  - deposite
  - withdraw
  -show details
  -show balance


'''


# class Bank:
    
# 	def __init__(self,name,age):
# 		print (f"welcome {name} and your is {age}")
# 		self.balance = 0
# 		self.name=name
# 		self.age= age

# 	def deposite(self,amount):
# 		self.balance +=amount
# 		print(f"your balance is {self.balance}")

# 	def withdraw(self,amount):
# 		if amount> self.balance:
# 			print(f"do you not have enough balance {self.balance}")
# 		else:
# 			self.balance-=amount
# 			print(f"your balance is {self.balance}")	
	    
# 	def show_details(self):
# 		print(f"hey {self.name} and your age is {self.age} your amount is {self.balance}")


	
# cli_1= Bank("moahemd", 20)
# cli_1.deposite(250)
# cli_1.withdraw(26)
# cli_1.show_details()




# from functools import reduce

# numbers = list(range(1,100))
# def mysum(x,y):
#     return x+y

# result = reduce(mysum, numbers)
# print(result)








# height = float(input("Your height in metres: "))
# weight = int(input("Your weight in kilograms: "))
# bmi = round(weight / (height*height) , 1)
# if bmi <= 18.5:
#     print("Your BMI is" , bmi , "which means you are a bit underweight.")
# elif bmi > 18.5 and bmi < 25:
#     print("Your BMI is" , bmi , "which means you are fit and healthy.")
# elif bmi > 25 and bmi < 30:
#     print("Your BMI is" , bmi , "which means you are a bit overweight.")
# elif bmi > 30:
#     print("Your BMI is" , bmi , "which means you are a bit obese.")
# else:
#     print("Invalid Input.")




# array = [10,161, 182 ,161 ,154 ,176, 170 ,167 ,171 ,170, 174]

# print(array)
# r = list(array)
# r.pop(0)
# print(r)
# result = set(r)
# print(result)
# result = sum(result) / len(result)
# # avarge = sum(array)/ len(array)

# print(result)


# def avarge(array):
#     r = list(array)
#     r.pop(0)
#     result = set(r)
#     result = sum(result) / len(result)
#     return result
# print(avarge([10,
# 161 ,182 ,161, 154, 176 ,170, 167, 171, 170 ,174]))


# def average(arr):
#     distinct_heights = set(arr)  # Create a set of distinct heights
#     sum_heights = sum(distinct_heights)  # Calculate the sum of distinct heights
#     num_heights = len(distinct_heights)  # Calculate the number of distinct heights
#     avg = sum_heights / num_heights  # Calculate the average
#     return round(avg, 3)  # Round the average to 3 decimal places

# # Read input
# n = int(input())
# heights = list(map(int, input().split()))

# # Calculate and print the average
# result = average(heights)
# print(result)
############################################################
# frontend 
# <iframe src="https://vk.com/video_ext.php?oid=786888529&id=456239886&hash=dabfa93fa377a62f" width="640" height="360" frameborder="0" allowfullscreen="1" allow="autoplay; encrypted-media; fullscreen; picture-in-picture"></iframe>



# exam python 












