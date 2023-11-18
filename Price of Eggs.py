#1.1. Prompt the user for the number of eggs.

eggs = int(input("How many eggs would you like to order?"))

#1.2. Calculate the number of dozens and loose eggs.

loose = eggs % 12
dozen = int((eggs - loose) / 12)

#1.3. Calculate the total cost.

costDozen = dozen * 3.25
costLoose = loose * 0.45
totalCost = costDozen + costLoose

#1.4. Display the final amount owed and order breakdown.
print("You ordered ", eggs, "egss. That's ", dozen, " at R3.25 per dozen and ",\
       loose, " loose eggs at 45c for a total of R", totalCost)