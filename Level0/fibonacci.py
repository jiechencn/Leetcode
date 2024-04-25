count = int(input("how many numbers?"))

print("method 1:", end=" ")
if count == 0:
    print("invalid input")
elif count == 1:
    print("0")
else:
    n1 = 0
    n2 = 1
    print(n1, n2, end=" ")
    for i in range(1, count-1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")

print("\nmethod 2:", end = " ")
fib = [0, 1]
for i in range(2, count):
    fib.append(fib[i-1] + fib[i-2])
print(fib)


def fib_func(n):
    if n == 1: 
        return 0
    elif n == 2:
        return 1
    else:
        return fib_func(n-1) + fib_func(n-2)
print("\nmethod 3:", end=" ")
for i in range(1, count+1):
    print(fib_func(i), end= " ")

