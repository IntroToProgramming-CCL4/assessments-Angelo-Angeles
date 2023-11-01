# Chapter 2 - Exercise 5, USB Shopper
Girl_money = 50
choice = input("Hello there! We have a special offer today! It's 6£ per USB, will you buy some? (Yes or No)\n")
if choice == "yes" or "Yes":
    print("Great! How many will you buy? You have 50£ right? That means you can buy", Girl_money // 6, "right now!")
    Number = int(input(""))
    if Number > 8:
        print("You cant buy that much!")
    elif Number <= 8:
        print("Great! That will be...", Number*6, "£, You will have", Girl_money - (Number*6), "£ Left!")
elif choice == "no" or "No":
    print("Well, okay then! See you later then!")
else:
    print("Sorry? I didnt catch that, I'll assume you wont, I'll see you later then!")