num = int(input("input a number:"))

if num < 2:
    print("not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number because", num, "=", num// i , "*", i)
            break
    else:
        print("prime number")