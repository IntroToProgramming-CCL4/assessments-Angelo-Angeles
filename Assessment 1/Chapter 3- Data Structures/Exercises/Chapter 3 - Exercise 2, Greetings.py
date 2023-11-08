# Chapter 3 - Exercise 2, Greetings

# This is the same way i made the list in exercise 1
names = []
Count = int(input("How many names do you want to print?\n"))
while Count != 0:
    userInput = input("\n\nWhat is the name?\n")
    names.append(userInput)
    Count = Count - 1

# This is the greetings for exercise 2, I am going to make a little easter egg if they input my name in...
for name in names:
    print ("I hope you have been well", name, "\n")
    if name == "Angelo":
        print("I greet my creator\n")