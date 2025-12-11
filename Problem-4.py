a = list(map(int,input("Enter a numbers ").split()))
b = {}

for i in range(1,10):
    count = 0
    for n in a:
        if n%i == 0:
            count += 1
    b[i] = count

print(b)
