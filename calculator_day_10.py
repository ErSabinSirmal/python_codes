#TODO -1 Write out the functions to caryy out the addition, multiplication, division and subtraction.
def add(n1, n2):
    return n1+n2

def multiply(n1,n2):
    return n1*n2

def division(n1,n2):
    return n1/n2

def sub(n1,n2):
    return n1-n2
#TODO: Add these 4 functions into a dictionary as values. Keys = "+","-","*","/"
operations = {
     "+":add,
     "-":sub,
     "*":multiply,
     "/":division,
     }

# print(operations["+"](5,6))


# this is the method 1 using the function but it can be done using while loop.....
def calculator():
    first_number = float(input("What is the first number?: "))
    should_accumulate = True
    while should_accumulate:
        print("+\n-\n*\n/\n")
        operation_symbol = input("Pick an opration: ")
        second_number = float(input("What is the next number?: "))
        answer = operations[operation_symbol](first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        choice = input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to start a new calculation:")

        if choice == "Y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n"*20) 
            calculator()   
calculator()