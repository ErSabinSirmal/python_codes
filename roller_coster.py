# multiple if statement example
print("Welcome to rollercoster!")
height = int(input("What is your height iin cm?"))
if height>=120:
  print("You can ride rollerconster: ")
  bill = 0
  age = int(input("What is your age? "))
  if age<12:
    bill = 5
    print("Child tickets are $5.")
  elif age<=18:
    bill = 7
    print("Youth tickets are $7. ")
  else:
    bill = 12
    print("Adult tickets are #12. ")

  wants_photo = input("Want photots? y or n ")
  if wants_photo =="y":
    bill+=3

  print(f"The total bill is ${bill} ")  

else:
  print("Sorry, you can't ride rollercoster: ")
