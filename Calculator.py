#CREATED BY - HARSH PRATAP SINGH PARIHAR
#TASK 2 - CALCULATOR


#Calculator 
print (".....WELCOME TO CALCULATOR!.....")
def sum(num1,num2):  
    return num1+num2 
def sub(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2==0:
         return "Error: Divide by Zero"
    return num1/num2

def calculator():
     num1=float(input("Enter the 1st number:"))
     num2=float(input("Enter the 2nd number:"))
     operation=input("Enter the operation (+, -, *, /): ")
     if operation == '+': 
         print(f"{num1} + {num2} = {sum(num1, num2)}") 
     elif operation == '-':
         print(f"{num1} - {num2} = {sub(num1, num2)}") 
     elif operation == '*': 
         print(f"{num1} * {num2} = {multiplication(num1, num2)}") 
     elif operation == '/':
         print(f"{num1} / {num2} = {div(num1, num2)}") 
     else: print("Invalid operation")
calculator()
