

print("Simple Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square (num1 squared)")

choice = int(input("Enter choice (1/2/3/4/5): "))

if choice == 1:
    print("Result =", num1 + num2)
    
elif choice == 2:
    print("Result =", num1 - num2)
    
elif choice == 3:
    print("Result =", num1 * num2)
    
elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
        
elif choice == 5:
    # square num1
    print("Result =", num1 ** 2)

else:
    print("Invalid Input")