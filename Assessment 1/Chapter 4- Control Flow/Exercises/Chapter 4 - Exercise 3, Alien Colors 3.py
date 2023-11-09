# Chapter 4 - Exercise 5, Alien Colors 3
player_name = input("Please enter your name:\n")
alien_color = ""

# I am making it a look so it asks the user again
while alien_color != "end":
    alien_color = input("Commander! There are several aliens nearby! Which one do you want to shoot?\n(Green, Red, Yellow)\n\n")
    alien_color.lower()
    if alien_color == "green" or "g":
        print("\n", player_name, "Has killed a GREEN alien and earned 5 points!")
        break
    elif alien_color == "yellow" or "y":
        print("\n", player_name, "Has killed a elite YELLOW alien and earned 10 points!")
        break
    elif alien_color == "red" or "r":
        print("\n", player_name, "Has killed a special RED alien and earned 15 points!")
        break
    else:
        print("\nSelect from Green, Yellow, or Red!\n\n")
        alien_color = "Again"