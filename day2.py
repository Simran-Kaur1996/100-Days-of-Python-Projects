# Data Types, Numbers , Operations, Types Conversion, f-Strings

#Subscripting
print("Hello"[0])

#String
print("123" + "345")

#Integer = whole number
print(123 + 345)

#Large Integer
print(1234556)

#Float = Floating Point Number
print(3.14159)

#Boolean
print(True)
print(False)

#len(s): return the length (the number of items) of a object.string,bytes,tuple,list,or range
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

#conversion
int()
float()
str()
bool()

#Number Manipulation
#bmi = 30.876565 => round(bmi)=> 31
#round(bmi,2)
#f-strings = we can use f-strings to insert a variable or an expression into a string

#final project = Tip Calculator Project

print("Welcome to the Tip Calculator")
bill = float(input("what was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people would you like? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print("Your total amount is:", final_amount)






