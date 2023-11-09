# Chapter 6 - Exercise 2, Movie Tickets

User_Input = input("Hello! Welcome to Angel Movies are you going to order a ticket?\n")
User_Input.lower()

if User_Input == "yes":
    User_Input = 1
    while User_Input != 0:
        User_Input = int(input("\n\nHow old are you sir? If you do not want to answer simply reply '0'\n"))
        if User_Input > 12:
            print("That will be 15$!\n")
        elif User_Input > 2:
            print("That will be 10$!\n")
        elif User_Input > 0:
            print("The ticket will be free!\n")
    print("Thank you for your patronage!")
print("Goodbye!")