# Chapter 7 - Exercise 3, T-Shirts

# Defining the function
def make_shirt(size, text):
    print("\nSo... What you're telling me is that you want a " + size, + " shirt with the print being, '" + text +"'? Alright.")

# User Input
Size = input("What size do you want your shirt to be? Small, Medium, Large, Extra Large?\n")
Text = input("\nAnd what text do you want to be printed on that shirt, huh?\n")

# Output
make_shirt(Size, Text)
make_shirt(text=Text, size=Size)