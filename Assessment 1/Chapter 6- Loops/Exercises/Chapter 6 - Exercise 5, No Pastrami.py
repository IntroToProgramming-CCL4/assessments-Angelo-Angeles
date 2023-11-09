# Chapter 6 - Exercise 5, No Pastrami
# I'm making it a little random
import random

sandwich_orders = ["Tuna Melt", "BLT", "Club Sandwich", "French Dip", "BBQ Beef Sandwich", "Pastrami", "Pastrami", "Pastrami"]
finished_sandwiches = []
random.shuffle(sandwich_orders)

# Removing Pastrami
print("FABBIANO: Ah BOSS! We ran out of Pastrami today! Looks like we gotta say it's sold out!\n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

# Sandwich making
for sandwich in sandwich_orders:
    print("BOSS:", sandwich, "coming right up! OI FABBIANNO! ONE", sandwich)
    finished_sandwiches.append(sandwich)
    print("FABBIANO: OI BOSS! One", sandwich, "done!\n")
print("BOSS: Ah workshift finally done eh Fabby? What did ya make today?\n\nFABBIANO: I finished a bunch! I listed them all down... Here!\n", finished_sandwiches)