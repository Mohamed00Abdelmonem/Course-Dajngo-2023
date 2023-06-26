# 10.Build a countdown calculator. Write some code that can take two dates as input, and
# then calculate the amount of time between them






# import datetime

# start_date = datetime.date(2023, 4, 24)
# end_date = datetime.date(2023, 5, 3)


# def countdown(start_date, end_date):
    
#     time_left = end_date - start_date
#     days = time_left.days
#     print(f"Time remaining: {days} days")


# countdown(start_date, end_date)









# 11. Make a temperature/measurement converter. Write a script that can convert
# Fahrenheit to Celcius and back, or inches to centimeters and back, etc in 3 different
# ways







# def convert_measurement(value, to_unit):
#     if to_unit == "inches":
#         return f"{value} * 2.54 = {value * 2.54:.3f} cm"
#     elif to_unit == "cm":
#         return f"{value} / 2.54 = {value / 2.54:.3f} inches"
# print(convert_measurement(20, "inches" ))    







# 12. Build an email slicer : create a function that takes an email as input and retrieve the
# username and domain of the email




# def slicer_email(email):
#     result = email.split("@")
#     return f"your username is : {result[0]} \n and your domin : {result[1]}"

# print(slicer_email("mmohamed@gamil.com"))









# 13. Currency converter : create a python script that takes a money with currency sign and
# convert it to some other currencies , the code should be like the game we did before





# i'm using in this example chat gpt


# class Currency:
#     def __init__(self, exchange_rate):
#         self.exchange_rate = exchange_rate

#     def convert_dollar(self, amount, currency_main):
#         converted_amount = amount / self.exchange_rate[currency_main]
#         return converted_amount

# # Example usage:
# exchange_rate = {'EUR': 0.85, 'EGP':0.03, 'JPY': 110.62}
# currency_converter = Currency(exchange_rate)

# # Call the method with the currency_main argument
# amount = 100
# currency_main = 'EGP'
# converted_amount = currency_converter.convert_dollar(amount, currency_main)
# print(f"{amount} dollars is {converted_amount:.2f} {currency_main}")










