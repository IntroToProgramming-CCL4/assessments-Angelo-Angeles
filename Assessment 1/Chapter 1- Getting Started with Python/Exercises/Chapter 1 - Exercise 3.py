print("\nExercise 3 - Print Date and Time\n")
# I will make this code output the current date and time for the user using the import datetime.
import datetime
d = datetime.datetime.now()
print("The current date and time is: ", d.strftime("%y-%m-%d %H:%m"))