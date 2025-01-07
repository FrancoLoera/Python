class Character:
    def __init__(self, name):
        self.name = name
        self.strenght = 100
        self.health = 1000
        
    def attack(self):
        return self.strenght
    
    def hit(self, points):
        self.health -= points
        
    def isAlive(self):
        if self.health > 0:
            return True
        
        else:
            return False
    
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health += 100
        self.strenght += 100

class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health -= 100
        self.strenght += 250
        
class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health -= 200
        self.strenght += 300
        
class BattleSimulator():
    def __init__(self, character1, character2):
        self.character1 = character1
        self.character2 = character2
    
    def battle(self):
        print("The battle begins now!\n")
        round_number = 1

        while self.character1.isAlive() and self.character2.isAlive():
            print(f"--- Round {round_number} ---")

            damage = self.character1.attack()
            self.character2.hit(damage)
            
            print(f"{self.character1.name} attacks {self.character2.name} dealing {damage} damage points.")
            
            if self.character2.health > 1:
                print(f"Remaining health of {self.character2.name}: {self.character2.health}")
            else:
                print(f"Remaining health of {self.character2.name}: 0")

            if not self.character2.isAlive():
                print(f"\n{self.character2.name} has fallen. ¡{self.character1.name} wins!")
                break

            damage = self.character2.attack()
            self.character1.hit(damage)
            print(f"{self.character2.name} attacks {self.character1.name} dealing {damage} damage points.")
            
            if self.character1.health > 1:
                print(f"Remaining health of {self.character1.name}: {self.character1.health}")
            else:
                print(f"Remaining health of {self.character1.name}: 0")

            if not self.character1.isAlive():
                print(f"\n{self.character1.name} has fallen. ¡{self.character2.name} wins!")
                break

            round_number += 1

        print("\nThe battle is over!")

characters = list()

for i in range(2):
    while True:
        name = input(f"Enter the Player {i + 1} character's name: ")
        print(f"{'\nCharacter Classes':<20}{'Health':<10}{'Damage':<10}")
        print(f"{'1- Warrior':<20}{'1,100':<10}{'200':<10}")
        print(f"{'2- Archer':<20}{'900':<10}{'350':<10}")
        print(f"{'3- Wizard':<20}{'800':<10}{'400':<10}")

        character_Class = int(input(f"\nSelect the Player {i + 1} character's class: "))
        match character_Class:
            case 1:
                characters.append(Warrior(name))
                break

            case 2:
                characters.append(Archer(name))
                break

            case 3:
                characters.append(Wizard(name))
                break

            case _:
                print("This isn't a valid option.")
                continue
    print()
            
driver = BattleSimulator(characters[0], characters[1])
driver.battle()