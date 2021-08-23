phone = input('Enter the phone : ')
digits_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for char in phone:
    output+= digits_mapping.get(char,"no not found") + " "
print(output)