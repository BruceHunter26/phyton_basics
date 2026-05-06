print("Simple Calculator")

num1 = float(input("Enter first number: ))
operator = input("Choose an operator (+, -, *,/): ")
num2 = float(input("Enter second number:"))

if operator == "+":
    print("Answer:",num1 + num2)
elif operator =="-":
    print("Answer:",num1 - num2)

elif operator =="*":
     print("Answer:",num1 * num2)
elif operator =="/":
   if num2 !=0:
       print("Answer:",num1 / num2)
    else:
       print("You cannot divide by zero.")

else:
     print("Invalid operator")
     
