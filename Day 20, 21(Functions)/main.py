def gmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


gmean(4, 5)
gmean(10, 20)


def average(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum / len(num))


average(1, 2, 3)
