# Chapter 6 - Exercise 1, Pizza Toppings
User_Input = input("Hello! Welcome to Angel's Pizza are you going to order a pizza?\n")
pizza = []

while User_Input == "yes" or "Yes":
    if User_Input == "quit":
        break
    User_Input.lower()
    User_Input = input("\n\nWhat topping do you want to be added? If you want to quit, just say so!\n")
    pizza.append(User_Input)
    if "quit" in pizza:
        pizza.remove("quit")
    print("Very well then! we shall add that to your pizza, your current toppings are:\n", pizza)
print("Thank you for your patronage!")