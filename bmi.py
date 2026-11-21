def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = (weight) / (height) * (height)
        

    if bmi < 18.5:
        print('Under Weight')
    elif bmi >= 18.5 and bmi <= 25.0:
        print('Normal Weight')
    elif bmi > 25.0:
        print('Over Weight')
    else:
        print('invalid')

    return bmi

bmi = calculate_bmi(weight=57, height=1.73)
print('bmi is= ' + str(bmi))