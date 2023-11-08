# Chapter 3 - Exercise 1, Names

# This is for user input so that the user can have their own list
names = []
Count = int(input("How many names do you want to print?\n"))
while Count != 0:
    userInput = input("\n\nWhat is the name?\n")
    names.append(userInput)
    Count = Count - 1

# This is the printing of names
for name in names:
    print("\n\nYour friend's name is:\n" + name)
