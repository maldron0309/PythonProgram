
def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("It cannot be divided by zero.")

def remainder(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        print("It cannot be divided by zero.")
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Remainder\n")

try:
    select = int(input("Select operations number : "))
except ValueError:
    print("Invalid entry, please enter a number.")
    exit()

try:
    number_1 = int(input("Enter first number : "))
    number_2 = int(input("Enter second number : "))
except ValueError:
    print("Invalid entry, please enter a number.")
    exit()

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1,number_2))

if select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1,number_2))
    
if select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1,number_2))
    
if select == 4:
    print(number_1, "/", number_2, "=", divide(number_1,number_2))
    
if select == 5:
    print(number_1, "%", number_2, "=", remainder(number_1,number_2))
    
else:
    print("Invalid input")

 
 
