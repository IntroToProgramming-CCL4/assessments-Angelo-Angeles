# Chapter 1 - Getting started with Python

print("\nExercise 1 -  Print Strings\n")
print("Twinkle, twinkle, little star,\n     How I wonder what you are!\n         Up above the world so high,\n          Like a diamond in the sky.\nTwinkle, twinkle, little star,\n     How I wonder what you are ")

print("\nExercise 2 - Print the Version of Python\n")
# I will make this code useable for any version of python the user is currently using, by using import platform.
import platform
print("Your version of python is: ", platform.python_version())

print("\nExercise 3 - Print Date and Time\n")
# I will make this code output the current date and time for the user using the import datetime.
import datetime
d = datetime.datetime.now()
print("The current date and time is: ", d.strftime("%y-%m-%d %H:%m"))

print("\nExercise 4 - Strings Concatination\n")
a, b, c = "A", "B", "C"
print(a, b, c)

print("\nExercise 5 - Compute Area of Circle\n")
Radius = float(input("Input the Radius of the Cicle: "))
print("The area of the circle is: ", 3.14*(Radius**2))