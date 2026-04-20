# 5. Weather Activity Suggestion
# Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
weather = "Sunny"

if weather == "Sunny":
    print("Go for a walk")
elif weather == "Rainy":
    print("Read a book")
elif weather == "Snowy":
    print("Build a snowman")
else:
    print("Enjoy your day!")
    
    
# OR

weather = "Sunny"

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(activity)