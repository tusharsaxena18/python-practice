w=int(input("Enter your weight"))
h=int(input("Enter your height"))
bmi=w/(h/100)**2
if (bmi<=18.5):
    print("UnderWeight")
elif (bmi>18.5 and   bmi<=24.9):
    print("Healthy")
elif (bmi>=25 and bmi<=29.9):
    print("OverWeight")
elif (bmi>30):
    print("Obese")
print('Your BMI is '+ str(bmi) + '.')