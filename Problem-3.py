a = int(input("Enter a number"))
b = a if a%2 != 0 else a-1
res = []
for i in range(1,b*2,2):
    res.append(i)
print(res)
