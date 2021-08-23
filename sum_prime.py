# num = int(input("Enter number till which you want sum of primes : "))
# l = []
# sum_prime = []
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#         list1.append(num)

# else:
#     print(num, "is not a prime number")
# sum_prime = sum(sum_prime)
# print(sum_prime)
# # for i in range(1, 10):

# #     for j in range(1, i):

# #         if i % j == 0 and i != j:

# #             l.append(i)
# # print(l)
# # print("sum : ", sum(l))

# # total = 0

# # for i in range(0, len(l)):

# #     total = total+l[i]


# # print("sum = ", total)
number = int(input("Enter number : "))
l1 = []
for num in range(1, number + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)
        l1.append(num)

print(l1)
total = sum(l1)
print(total)
