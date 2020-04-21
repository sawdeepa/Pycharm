import math
h=int(input("height(in cms)"))
w=int(input("weight(in kgs)"))
bmi=(round(w / ( (h/100)**2),2))
print(bmi)
if bmi <19:
    print("Under weight")
elif bmi >= 19 and bmi <= 29 :
    print("Normal")
elif bmi >= 29 and bmi <= 39 :
    print("Overweight")
else :
    print("Obese")


