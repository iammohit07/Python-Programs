# list_fruit = []
# i = 0
# while i < 7:
#     fruits = input('Enter the Fruit : ')
#     list_fruit.append(fruits)
#     i+=1
# print(list_fruit)
# marks = []
# final_marks = []
# num = []
# i = 0
# while i < 5:
#     mark = input('Enter the Marks of student  : ')
#     marks.append(mark)
#     i+=1
# marks.sort()
# print(marks)
list = []
i = 0
print('Enter the Marks of student  : ')
while i < 5:
    val = int(input(''))
    list.append(val)
    i+=1
print('list : ',list)
res = [(val,pow(val,3)) for val in list]
print('List in tuple form : ',res) 