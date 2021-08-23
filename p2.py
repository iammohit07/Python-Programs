name = str(input('Enter your name  :'))
color =str(input('Enter your fav color  :'))
result = f'fav volor of  {name} is  {color}' #formatting string
print(result)
find_word = str(input('Enter word or letter to find '))
# find in result
print(result.find(find_word))
print(find_word in result)
# weight =int(input('enter your weight : '))
# weight_in_kg = 0.453592*weight
# print('weight in kg is :' ,weight_in_kg)