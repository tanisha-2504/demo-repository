print("welcome to the interactive personal data collector!")

name = input("please enter your name : ")
age = int(input("please enter your age : "))
height = float(input("please enter your height in meters : "))
number = int(input("please enter your fav number : "))

print(name and age and height and number )
print("Thank you! Here is the information we collected:")

print("Name:", name, "(Type:", type(name), ", Memory Address:", id(name), ")")
print("Age:", age, "(Type:", type(age), ", Memory Address:", id(age), ")")
print("Height:", height, "(Type:", type(height), ", Memory Address:", id(height), ")")
print("Fav Number:", number, "(Type:", type(number), ", Memory Address:", id(number), ")")

birth_year = 2026 - age
print("your birth year is approximately : ", birth_year, "(based on your age of", age, ")")
print ("Thank you for using the Personal Data Collector. Goodbye!")