# matrix = [
#     [2,2,3],
#     [4,5,5],
#     [6,7,8]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
# removing dupicates from list
numbers = [2,42,2,42,31,1,3,45,6,54,32,2,2,3,4,5,45]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
uniques.sort()
print(f'sorted unique or list after removing duplicates is {uniques}')