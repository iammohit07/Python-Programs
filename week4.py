input_list = []
final_list = []
n = input('')
n = int(n)
for n in range(0, n):
    val = input('').split()
    input_list.append(val)
print('list : ', input_list)
list1 = int(input_list)
for i in list1:
    if (i % 10) != 4:
        final_list.append(i)
print(final_list)
print(input_list)
