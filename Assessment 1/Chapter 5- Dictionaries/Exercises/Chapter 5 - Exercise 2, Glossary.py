# Chapter 5 - Exercise 2, Glossary
Glossary = {
    "Integer":"A integer is data type that is a number without decimals/float points.",
    "Float":"A float is a data type that is a number with decimals/float points.",
    "String":"A string is a data type that is a set of characters/letters/words.",
    "Variable":"A variable is a place to store a one value regardless of data type.",
    "List":"A list is a place to store multiple values regardless of data type."
}

# To print the dictionary better and neater
for keyword, meaning in Glossary.items():
    print("{}\n{}\n\n".format(keyword, meaning))