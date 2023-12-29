# Displaying the operations that can be done by calculator
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Enter the operation index choice from the display
choice=input("Enter choice (1/2/3/4): ")

#Entering the input numbers on which operations need to be performed
if choice in['1','2','3','4']:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    
    #Addition
    if choice=='1':
        result=num1+num2
        print(f"{num1}+{num2}={result}")
        
    #Substraction
    elif choice=='2':
        result=num1-num2
        print(f"{num1}-{num2}={result}")

    #Multiplication
    elif choice=='3':
        result=num1*num2
        print(f"{num1}*{num2}={result}")

    #Division
    elif choice=='4':
        if num2!=0:
            result=num1/num2
            print(f"{num1}/{num2}={result}")
        else:
            print("Cannot divide by zero.")
            
#If the opertion is not available on the display
else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")

