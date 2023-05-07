height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_data = weight/(height*height)
bmi_data = round(bmi_data)
if bmi_data < 18.5:
    print("У вас недостаточный вес")
elif bmi_data >18.5 and bmi_data < 25:
    print("У вас нормальный вес")
elif bmi_data > 25 and bmi_data < 30:
    print("У вас ожирение")
else:
    print("У вас клиническое ожирение")