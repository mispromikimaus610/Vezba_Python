num1:float = float(input("Enter the first number: "))
operator: str = input("enter the operator(+; -; *; /): ")
num2:float = float(input("Enter the second number: "))

if(operator == "+"):
    print(f"The result is {num1+num2}")
elif(operator == "-"):
    print(f"The result is {num1-num2}")
elif(operator == "*"):
    print(f"The result is {num1*num2}")
elif(operator == "/"):
    print(f"The result is {num1/num2}")
else:
    print("Invalid operator")