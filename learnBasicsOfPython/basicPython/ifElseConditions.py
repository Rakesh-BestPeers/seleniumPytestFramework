height = float(input("Enter Height : "))
weight = float(input("Enter Weight : "))

bmi_index = weight / height ** 2

if bmi_index < 0:
    print("System Error")
elif bmi_index > 25:
    print("OK")

elif bmi_index > 50:
    print("Good")

else:
    print("Out of Scope")
