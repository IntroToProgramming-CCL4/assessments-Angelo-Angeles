# Chapter 3 - Exercise 7, Seeing the world

locations = []
Count = 1

# This is to have user input
while Count != 0:
    Count = int(input("How many locations do you want to visit?\n"))
    if Count >= 5:
        while Count != 0:
            userInput = input("\n\nWhat is the location name?\n")
            locations.append(userInput)
            Count = Count - 1
    elif Count == 0:
        print("\n\nWe wont go anywhere then.")
        exit()
    else:
        print("\n\nPlease think of atleast 5...\n")

# Temporary change of order
print("List Order Change Test:\n\n", "Original:", locations, "\n", "Alphabetically sorted:", sorted(locations), "\n\n", "Original:", locations, "\n\n", "Reverse Alphabetically sorted:", sorted(locations, reverse=True), "\n", "Original:", locations, "\n")

# Using Reverse() which is permanent
locations.reverse()
print(locations)
locations.reverse()
print(locations)

# Using Sort() which is permanent
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)