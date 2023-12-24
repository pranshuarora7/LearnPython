import time

timestamp = time.strftime("%H:%M:%S")
print("current time is", timestamp)
h = int(time.strftime("%H"))
m = time.strftime("%M")
s = time.strftime("%S")

if h > 20:
    print("It's too late! Go to bed.")
elif h < 12:
    print("Goodmorning")
elif h >= 12 and h < 16:
    print("good afternoon")
else:
    print("good evening")
