# Chapter 3 - Exercise 6, Shrinking Guest List
names = []
Count = 1

# This is to have user input
while Count != 0:
    Count = int(input("How many guests do you want to invite?\n"))
    FutureCount = Count
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

# Start of Exercise 5
# This is to add random elements.
import random


print("\n\n\nHello, dear guests. Sadly tonight", names[1], "is not present as they have had a sudden change of plans. Do not worry however, as we have already solved the situation.")

# This is to remove an element from my list
names.pop(1)

# This is my reserve guests that i can add to my list
Reserve_Guests = ["APPLe", "Regulus", "Vertin"]

# I pick randomly from my reserve guests
Invited_Reserve = random.choice(Reserve_Guests)
names.insert(1, Invited_Reserve)

# New invites given to the guests
for name in names:
    print("\nThank you for your patience! We humbly invite", name, "to our dinner party this friday!")


# This is the start of Exercise 6
print("\n\n\nHello dear guests, sadly due to budget constraints we are only able to accomodate 2 guests... Sorry for the inconvenience")

# Purging the list down to 2!
random.shuffle(names)
FutureCount = FutureCount - 2
while FutureCount != 0:
    names.pop(1)
    FutureCount = FutureCount - 1

# Sending out the invites again!
for name in names:
    print("\nHello", name, "you are still invited to friday's dinner party! See you there!\n")

# Clearing my list
names.clear()
print("\nMy list is:\n", names)