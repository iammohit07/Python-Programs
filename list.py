a = []
new = []
n = int(input(''))
for i in range(0, n):
    elm = int(input(""))
    i += 1
    a.append(elm)
print(" a[] : ",a)
for j in range(0,len(a)):
    new.append(a[a[j]])
print(new)
