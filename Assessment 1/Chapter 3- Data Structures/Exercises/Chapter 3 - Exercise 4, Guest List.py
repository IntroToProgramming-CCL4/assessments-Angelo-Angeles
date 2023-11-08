# Chapter 3 - Exercise 4, Guest List
names = []
Count = 1

# This is to have user input
while Count != 0:
    Count = int(input("How many guests do you want to invite?\n"))
    if Count >= 3:
        while Count != 0:
            userInput = input("\n\nWhat is the guest's name?\n")
            names.append(userInput)
            Count = Count - 1
    elif Count == 0:
        print("\n\nWe shall not have a dinner party then.")
        exit()
    else:
        print("\n\nPlease invite more than 2 guests\n")

# This is to print the invite
for name in names:
    print("\nHello", name, "We humbly invite you to our dinner party on friday.")