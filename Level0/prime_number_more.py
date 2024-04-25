maxnumer = int(input("Enter the maximum number: "))
for num in range(2, maxnumer):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
