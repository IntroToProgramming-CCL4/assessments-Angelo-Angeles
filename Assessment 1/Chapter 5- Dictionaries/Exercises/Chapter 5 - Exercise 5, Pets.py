# Chapter 5 - Exercise 5, Pets
Dogs = {
    "Labrador":"Jonathan",
    "Husky":"Casey",
    "Golden Retriever":"Bravo"
}

Cats = {
    "Persian":"Hershey",
    "Orange Tabby":"Samantha",
    "British Shorthair":"Louie"
}

Snakes = {
    "Ball Python":"Johnson",
    "Boa Constrictor":"Angelo",
    "Corn Snake":"Rembrandt"
}

# This will be checking for each pet type and each pet in each pet type so that it can print out designated lines per pet! 
Pets = [Dogs, Cats, Snakes]
for pet_type in Pets:
    if pet_type is Dogs:
        print("Dogs:\n\n")
        for pet, owner in Dogs.items():
            print("Dog Breed: {}\nOwner: {}".format(pet, owner))
            if pet == "Labrador":
                print("\nPersonality: Active, Outgoing, Extroverted, and Passionate dogs that guarantee a fun time playing and walking.\n\n")
            elif pet == "Husky":
                print("\nPersonality: Independent, Loud, Playful, and Mischievous dogs that will make you question why you brought her in and then also make you realize it's becuase she's very very fun.\n\n")
            elif pet == "Golden Retriever":
                print("\nPersonality: Trustworthy, Eager, Extroverted, and Outgoing dogs that will brighten any day with their cozy ness and energy.\n\n")
    if pet_type is Cats:
        print("Cats:\n\n")
        for pet, owner in Cats.items():
            print("Cat Breed: {}\nOwner: {}".format(pet, owner))
            if pet == "Persian":
                print("\nPersonality: Quiet and Affectionate cats who enjoy being pet, lounging around, and being held.\n\n")
            elif pet == "Orange Tabby":
                print("\nPersonality: Curious and Friendly cats that are often known to be the chattiest and friendliest among alot of breeds!\n\n")
            elif pet == "British Shorthair":
                print("\nPersonality: Loyal and Loving cats that are quite well behaved if you respect them and their cat... needs?\n\n")
    if pet_type is Snakes:
        print("Snakes:\n\n")
        for pet, owner in Snakes.items():
            print("Snake Breed: {}\nOwner: {}".format(pet, owner))
            if pet == "Ball Python":
                print("\nPersonality: Nocturnal and Sensitive to temps, these snakes often ball up when they feel threatened, thus the name 'Ball Python'\n\n")
            elif pet == "Boa Constrictor":
                print("\nPersonality: Large and Friendly snakes that enjoy being held in the hands of the owner!\n\n")
            elif pet == "Corn Snake":
                print("\nPersonality: Docile and Friednly snakes that are often considered the best first choice for a pet snake due to its calm temperance and personality.\n\n")