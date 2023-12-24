questions = [
    "Question 1",
    "Quesstion 2",
    "Question 3",
    "Question 4",
    "Quesstion 5",
    "Question 6",
    "Question 7",
]
answers = ["A", "B", "C", "A", "B", "C", "D"]

i = 0
sum = 0
for i in range(len(questions)):
    print("Question ", i + 1, ":", questions[i])
    answer = input("Write Correct option: A, B, C, D \n")
    if answers[i] == answer:
        sum = sum + ((i + 1) * 1000)
        print("congrats write answer, your total price money is :", sum)
        i = i + 1
    else:
        print("sorry your answer is wrong the correct answer was :", answers[i], "\n")
        print("Your total price money is :", sum)
        break
print("thank you")
