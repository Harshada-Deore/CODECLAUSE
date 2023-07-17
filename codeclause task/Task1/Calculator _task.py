#Calculator in python
# Python program for simple calculator
 
# Function to addition two numbers
def addition(num1, num2):
    return num1 + num2
 
# Function to subtraction two numbers
def subtraction(num1, num2):
    return num1 - num2
 
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
 
print("Please select operation -\n" \
        "1. Addition\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
 
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
 
if select == 1:
    print(number1, "+", number2, "=",
                    addition(number1, number2))
 
elif select == 2:
    print(number1, "-", number2, "=",
                    subtraction(number1, number2))
 
elif select == 3:
    print(number1, "*", number2, "=",
                    multiply(number1, number2))
 
elif select == 4:
    print(number1, "/", number2, "=",
                    divide(number1, number2))
else:
    print("Invalid input")