def add(x,y):
    sum = x+y
    print(f"The sum of the numbers is: {sum}")

def sub(x,y):
    subt = x-y
    print(f"The substraction of the numbers is: {subt}")

def division(x,y):
    div = x/y
    print(f"The division of the numbers is : {div}")

def calculator():
    print("Menu:\n")
    print("1. Addition of two numbers: \n")
    print("2. Subtraction of two numbers: \n")
    print("3. Division of two numbers: \n")

    choice = int(input("Enter your choice (1/2/3): "))
    if choice<=3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice == 1:
            add(num1,num2)

        if choice == 2:
            sub(num1,num2)

        if choice == 3: 
            division(num1, num2)


calculator()                   
    


