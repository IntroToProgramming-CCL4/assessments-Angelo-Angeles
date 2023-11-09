# Chapter 4 - Exercise 2, Alien Colors 2

# Just basics part 2
player_name = input("Please enter your name:\n")
alien_color = input("Commander! There are several aliens nearby! Which one do you want to shoot?\n(Green, Red, Yellow)\n\n")
if alien_color == "Green":
    print(player_name, "\nHas earned 5 points!")
else:
    print(player_name, "\nHas earned 10 points!")
