age = int(input("Enter your age: "))

print(age > 18)
print(age < 18)
print(age == 18)
print(age != 18)

if age >= 18 and age < 21:
    print("You can buy but you cannot drink, Wait for", 21 - age, "years")
elif age >= 21:
    print("you can drink")
else:
    print("Papa ko bataun,", 18 - age, "saal rukja phle")
