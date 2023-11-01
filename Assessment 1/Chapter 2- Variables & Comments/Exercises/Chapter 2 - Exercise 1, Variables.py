# Chapter 2 - Exercise 1, Variables

# I want the user to have control over how many times they type a message and it gets repeated to them so i made it a loop
Count = int(input("Input how many times you want to type your message:\n"))
while Count != 0:
    Message = input("\nPlease input a message you want to be printed out:\n")
    print("\nThis is your message:\n" + Message.strip())
    Count = Count - 1