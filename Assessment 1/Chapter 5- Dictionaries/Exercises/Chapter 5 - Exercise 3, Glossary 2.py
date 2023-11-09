# Chapter 5 - Exercise 3, Glossary 2
Glossary = {
    "Integer":"A integer is data type that is a number without decimals/float points.",
    "Float":"A float is a data type that is a number with decimals/float points.",
    "String":"A string is a data type that is a set of characters/letters/words.",
    "Variable":"A variable is a place to store a one value regardless of data type.",
    "List":"A list is a place to store multiple values regardless of data type.",
    "Program":"A program is a set of instructions that a computer uses to perform a specific action.",
    "Tuple":"Tuples act like a list, but they can't be mutated.",
    "Object":"Any 'thing' in Python. An object represents data has attributes and methods.",
    "Mutable":"An object that can be changed (i.e. mutated). The 'value' of a mutable object can change (meaning the data it contains)",
    "Callable":"An object which can be 'called'. If you have a variable that represents a callable object, you can 'call' that object by putting parentheses after it (e.g. like_this()). \nAny arguments passed to that callable, should be put inside the parentheses."
}


# I never really used print() in the previous exercise so... I will just continue using this...
for keyword, meaning in Glossary.items():
    print("{}\n{}\n\n".format(keyword, meaning))
