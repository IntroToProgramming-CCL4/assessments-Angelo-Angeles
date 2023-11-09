# Chapter 6 - Exercise 4, Deli
sandwich_orders = ["Tuna Melt", "BLT", "Club Sandwich", "French Dip", "BBQ Beef Sandwich", "Pastrami"]
finished_sandwiches = []

# Sandwich making
for sandwich in sandwich_orders:
    print("BOSS:", sandwich, "coming right up! OI FABBIANNO! ONE", sandwich)
    finished_sandwiches.append(sandwich)
    print("FABBIANO: OI BOSS! One", sandwich, "done!\n")
print("BOSS: Ah workshift finally done eh Fabby? What did ya make today?\n\nFABBIANO: I finished a bunch! I listed them all down... Here!\n", finished_sandwiches)