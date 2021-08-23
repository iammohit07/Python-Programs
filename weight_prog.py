weight = int(input('Enter your weight : '))
unit = str(input('Weight is in Lbs or Kg : '))
if unit.lower() == "lbs" :
    print('Weight in kg : ', weight*0.45)
else:
    print('Weight in Lbs : ', weight*2.2)