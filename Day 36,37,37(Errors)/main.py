def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


x = input("Enter a number: ")
try:
    print(fact(x))
except:
    print("invalid input")
