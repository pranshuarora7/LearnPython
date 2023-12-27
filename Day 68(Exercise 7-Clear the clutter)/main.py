import os

files = os.listdir("Day 68(Exercise 7-Clear the clutter)/Wallpaper")
i = 1
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(
            f"Day 68(Exercise 7-Clear the clutter)/Wallpaper/{file}",
            f"Day 68(Exercise 7-Clear the clutter)/Wallpaper/{i}.jpg",
        )
        i = i + 1
