# Chapter 2 - Exercise 2, Variables PART 2 ELECTRIC BOGALOO
import random
# I'm importing random because i want random qoutes from a selected list

# I'm making it a loop because I want it when the user inputs something aside from the inputs i want it loops
End = 1
while End != 0:
    Who = input("Pick a person to get a qoute from:\nMori Calliope (1)\nMartin Luther King Jr (2)\nSun Tzu (3)\n\n")
    Who = Who.strip()
    if Who == "1":
        Qoute = ["“If you quit when you suck, you'll suck forever”", "“We never forget the fallen, but we move on.”", "“Based.”"]
        random.shuffle(Qoute)
        print ("\nMori Calliope once said", Qoute[1])
        break
    elif Who == "2":
        Qoute = ["“Darkness cannot drive out darkness, only light can do that. Hate cannot drive out hate, only love can do that.”", "“The ultimate measure of a man is not where he stands in moments of comfort and convenience, but where he stands at times of challenge and controversy.”", "“True peace is not merely the absence of tension; it is the presence of justice.”"]
        random.shuffle(Qoute)
        print ("\nMartin Luther King Jr once said", Qoute[1])
        break
    elif Who == "3":
        Qoute = ["“He will win who knows when to fight and when not to fight.”", "“Opportunities multiply as they are seized.”", "“Know yourself and you will win all battles.”"]
        random.shuffle(Qoute)
        print ("\nSun Tzu once said", Qoute[1])
        break
    else:
        print("You did not select one of the persons properly.")
print("\nThank you for your participation.")