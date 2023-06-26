height = float(input("Your height in metres: "))
weight = int(input("Your weight in kilograms: "))
bmi = round(weight / (height*height) , 1)
if bmi <= 18.5:
    print("Your BMI is" , bmi , "which means you are a bit underweight.")
elif bmi > 18.5 and bmi < 25:
    print("Your BMI is" , bmi , "which means you are fit and healthy.")
elif bmi > 25 and bmi < 30:
    print("Your BMI is" , bmi , "which means you are a bit overweight.")
elif bmi > 30:
    print("Your BMI is" , bmi , "which means you are a bit obese.")
else:
    print("Invalid Input.")
