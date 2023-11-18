import random

#3.1. Define a Monster class.
class monster():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp        

    def attack(self, atk):
        self.atk = random.randint(1, 20)
        atk = self.atk
        return atk
    
#3.2. Define a Player class.
class player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, atk):
        self.atk = random.randint(1, 20)
        atk = self.atk
        return atk
    
#3.3. Define a main function.

def main():
    print("Welcome to the Monster game!")


if __name__ == "__main__":
    main()

#3.4. Create a new monster and player instance.

Monster = monster("Monster", 50)
Player = player("Player", 100)

#3.5.	Loop until either the monster or player is defeated.

pHP = Player.hp
mHP = Monster.hp

while pHP > 0 and mHP > 0:
    print("Player HP: ", pHP, " | Monster HP : ", mHP) #3.6. Display the current HP for both the monster and player.

    pAttack = Player.attack(random.randint(0, 20))
    mAttack = Monster.attack(random.randint(0, 50))

    print(Player.name, " attacks ", Monster.name, "for ", pAttack, " damage")
    print(Monster.name, " attacks ", Player.name, "for ", mAttack, " damage")

    pHP = pHP - mAttack
    mHP = mHP - pAttack


if mHP <= 0:
    print(Player.name, " has defaeted ", Monster.name)

else:
    print(Monster.name, " has defeated ", Player.name)