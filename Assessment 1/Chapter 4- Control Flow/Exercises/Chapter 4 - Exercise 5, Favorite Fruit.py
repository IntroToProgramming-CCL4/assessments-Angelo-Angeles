# Chapter 4 - Exercise 5, Favorite Fruit
favorite_fruits = []
Count = 1

# This is to have user input
while Count != 0:
    Count = int(input("How many favorite fruits do you have?\n"))
    if Count >= 3:
        while Count != 0:
            userInput = input("\n\nWhat is the name of the fruit?\n")
            favorite_fruits.append(userInput)
            Count = Count - 1
    elif Count == 0:
        print("\n\nYou dont have any? Okay then.")
        exit()
    else:
        print("\n\nAtleast think of three...\n")

# Making a definition to lowercase every element in the list so it's easier to check
def lowercase(List):
    return[x.lower() for x in List]
lowercase(favorite_fruits)


# I am just following orders and checking with 5 ifs
if "mango" or "mangos" in favorite_fruits:
    print("\nYou like mangos too?")
if "apple" or "apples" in favorite_fruits:
    print("\nYou like apples too?")
if "peach" or "peaches" in favorite_fruits:
    print("\nYou like peaches too?")
if "lychee" or "lychees" in favorite_fruits:
    print("\nYou like lychees too?")
if "pear" or "pears" in favorite_fruits:
    print("\nYou like pears too?")