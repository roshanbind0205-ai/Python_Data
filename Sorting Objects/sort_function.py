numbers=[5,4,2,6]
n=len(numbers)

for i in range(n):
    for j in range(0,n-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(numbers)