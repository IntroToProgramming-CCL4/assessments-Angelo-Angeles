# Chapter 4 - Exercise 4, Stages of Life
Player_Age = int(input("How old are you?\n"))

# There doesnt seem to be a more effective way to do if-elif chains other than this... It is long though.
if Player_Age < 0:
    print("You dont exist")
elif Player_Age >= 65:
    print("You are a elder.")
elif Player_Age >= 20:
    print("You are a adult.")
elif Player_Age >= 13:
    print("You are a teenager.")
elif Player_Age >= 4:
    print("You are a kid.")
elif Player_Age >= 2:
    print("You are a toddler.")
elif Player_Age < 2:
    print("You are a baby.")