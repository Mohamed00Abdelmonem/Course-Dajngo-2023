
# oop

'''
Bank

  - create clinet (name , age )
  - deposite
  - withdraw
  -show details
  -show balance


'''



class Bank:
    
	def __init__(self,name,age):
		print (f"welcome {name} and your is {age}")
		self.balance = 0
		self.name=name
		self.age= age

	def deposite(self,amount):
		self.balance +=amount
		print(f"your balance is {self.balance}")

	def withdraw(self,amount):
		if amount> self.balance:
			print(f"do you not have enough balance {self.balance}")
		else:
			self.balance-=amount
			print(f"your balance is {self.balance}")	
	    
	def show_details(self):
		print(f"hey {self.name} and your age is {self.age} your amount is {self.balance}")


	
cli_1= Bank("moahemd", 20)
cli_1.deposite(250)
cli_1.withdraw(26)
cli_1.show_details()


