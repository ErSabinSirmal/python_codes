#BMI calculator.....
# Enter your height in meters e.g., 1.55
height = float(input("Enter your height in meters:"))
weight = int(input("Enter your weight in kgs: "))

#calculating the body mass index..
bmi = weight/height**2
if bmi<18.5:
 print(f"Your BMI is {bmi}, you are underweight." )
elif bmi<25:
 print(f"Your BMI is {bmi}, you have a normal weight." )
elif bmi<30:
 print(f"Your BMI is {bmi}, you are slightly overweight." )
elif bmi<35:
 print(f"Your BMI is {bmi}, you are obese." )
elif bmi>=35:
 print(f"Your BMI is {bmi}, you are clinically obese." )