weight = 65
height = 1.60

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
elif bmi <= 24.9:
    print("normal weight")
else:
    print("overweight")
