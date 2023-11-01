# Chapter 2 - Exercise 3, Stripping Names
# I ran out of ideas how to make this unique
Name = "\tAngelo Ivan Lemuel R Angeles          "
print("My name is: ", Name, "Oh, it seems like there are excess spaces let me remove them...\n")
print("Let's try .rstrip then!", Name.rstrip(), "Oh that only just removed the spaces after my name... Let me try again.\n")
print("Let's try .lstrip then...", Name.lstrip(), " Well, that only removed the spaces before my name... LETS TRY THIS AGAIN!\n")
print("Let's finally try just .strip()", Name.strip(), "OKAY FINALLY. Thats my name.\n")