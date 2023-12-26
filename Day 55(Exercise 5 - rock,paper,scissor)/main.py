import random


def play(n, c):
    if n == c:
        print("It is a tie")
    if n == 1 and c == 2:
        print("You won")
    if n == 1 and c == 3:
        print("Computer wins")
    if n == 2 and c == 1:
        print("Computer wins")
    if n == 2 and c == 3:
        print("You won")
    if n == 3 and c == 1:
        print("You won")
    if n == 3 and c == 2:
        print("Computer wins")


print("\t1.Rock")
print("\t2.Paper")
print("\t3.Scissor")
c = int(input("Enter your choice: "))
n = random.randint(1, 3)

play(n, c)
