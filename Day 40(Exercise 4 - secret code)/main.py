def reverse(x):
    return x[::-1]


x = input("Enter a word \n")


def encrypt(x):
    if len(x) > 3:
        d = "sas" + x[1:] + x[0] + "fgd"
    else:
        d = reverse(x)
    print(d)


def decrypt(x):
    if len(x) < 3:
        d = reverse(x)
    else:
        d = x[-4] + x[3 : len(x) - 4]
    print(d)


c = int(input("Enter 1 for coding and 2 for decoding \n"))
if c == 1:
    encrypt(x)
elif c == 2:
    decrypt(x)
else:
    print("Invalid Input")
