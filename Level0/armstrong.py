maxnum = int(input("Enter the maximum number: "))

for num in range(0, maxnum+1):
    len = (str(num).__len__())
    temp = num
    sum = 0
    for i in range(len):
        right = temp % 10
        temp = temp // 10
        sum = sum + right ** len
    if sum == num:
        print(num, end=" ")
    

