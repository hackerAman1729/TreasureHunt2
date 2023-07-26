class Game:
    def __init__(self):
        self.alive = True
        self.has_treasure = False
        self.friends = 0
        self.clue = False
        self.location = "boat"

    def start(self):
        print("Welcome to the Island Adventure Game!")
        print("You're starting your journey on a boat, sailing toward an uncharted island...")

        while self.alive and not self.has_treasure:
            if self.location == "boat":
                self.boat_scene()
            elif self.location == "island":
                self.island_scene()
            elif self.location == "jungle":
                self.jungle_scene()
            elif self.location == "cave":
                self.cave_scene()
            elif self.location == "mountain":
                self.mountain_scene()
            elif self.location == "zombie_scene":
                self.zombie_scene()
            elif self.location == "zombie_battle":
                self.zombie_battle_scene()
            elif self.location == "treasure_hunt":
                self.treasure_hunt_scene()
            else:
                print("An error occurred...")

        if self.alive and self.has_treasure:
            print("Congratulations! You survived and found the treasure!")
        elif not self.alive:
            print("You have died. Better luck next time!")

    def boat_scene(self):
        print("While on the boat, you see a group of pirates approaching...")
        decision = input("Do you want to fight (f) the pirates or befriend (b) them? ")

        if decision.lower() == "f":
            print("You decided to fight the pirates, but they were too strong.")
            self.alive = False
        elif decision.lower() == "b":
            print("You decided to befriend the pirates. They turn out to be friendly and join your cause.")
            self.friends += 1
            self.location = "island"
        else:
            print("Invalid decision. Please choose either 'f' or 'b'.")

    def island_scene(self):
        print("You've reached the island. It's a beautiful place filled with dense jungle and towering mountains.")
        decision = input("Do you want to explore (e) the jungle or climb (c) the mountain? ")

        if decision.lower() == "e":
            self.location = "jungle"
        elif decision.lower() == "c":
            self.location = "mountain"
        else:
            print("Invalid decision. Please choose either 'e' or 'c'.")

    def jungle_scene(self):
        print("Inside the jungle, you meet a local inhabitant...")
        decision = input("Do you want to befriend (b) the inhabitant or ignore (i) them? ")

        if decision.lower() == "b":
            print("You decided to befriend the inhabitant. They offer to help you in your journey.")
            self.friends += 1
            self.location = "cave"
        elif decision.lower() == "i":
            print("You decided to ignore the inhabitant and continue on your own.")
            print("You're really hungry. There are some berries nearby...")
            decision = input("Do you want to eat (e) the berries or not eat (n) them? ")

            if decision.lower() == "e":
                print("You ate the berries, but they were poisonous...")
                self.alive = False
            elif decision.lower() == "n":
                print("You decided not to eat the berries. But without food, you couldn't survive...")
                self.alive = False
            else:
                print("Invalid decision. Please choose either 'e' or 'n'.")
        else:
            print("Invalid decision. Please choose either 'b' or 'i'.")

    def cave_scene(self):
        print("You see a cave nearby...")
        decision = input("Do you want to rest (r) in the cave or explore (e) it? ")

        if decision.lower() == "r":
            print("You decided to rest in the cave and prepare for the journey ahead.")
            self.location = "zombie_scene"
        elif decision.lower() == "e":
            print("You decided to explore the cave. You find a clue to the treasure chest's riddle!")
            self.clue = True
            self.location = "zombie_scene"
        else:
            print("Invalid decision. Please choose either 'r' or 'e'.")

    def mountain_scene(self):
        print("You're climbing the mountain. At the top, you meet an old hermit...")
        decision = input("Do you want to ask the hermit for advice (a), give him some food (f), or leave (l)? ")

        if decision.lower() == "a":
            print("The hermit tells you a legend about the island's treasure. This might help you later...")
            self.clue = True
            print("After your encounter with the hermit, you start your descent down the mountain. As you reach the base, you suddenly hear strange noises...")
            self.location = "zombie_scene"
        elif decision.lower() == "f":
            print("The hermit is grateful for the food. In return, he offers to join you on your journey.")
            self.friends += 1
            print("With the hermit now part of your team, you start your descent down the mountain. As you reach the base, you suddenly hear strange noises...")
            self.location = "zombie_scene"
        elif decision.lower() == "l":
            print("You decided to leave the hermit and continue on your own. As you descend, you encounter a horde of zombies...")
            self.location = "zombie_scene"
        else:
            print("Invalid decision. Please choose either 'a', 'f', or 'l'.")

    def zombie_scene(self):
        print("You see a horde of zombies approaching...")
        decision = input("Do you want to run (r) or fight (f) the zombies? ")

        if decision.lower() == "r":
            print("You decided to run, but the zombies were too fast and caught up with you.")
            self.alive = False
        elif decision.lower() == "f":
            print("You decided to stand your ground and fight the zombies.")
            self.location = "zombie_battle"
        else:
            print("Invalid decision. Please choose either 'r' or 'f'.")

    def zombie_battle_scene(self):
        print(f"You're fighting the zombies with your {self.friends} friend(s)...")

        if self.friends >= 2:
            print("You and your friends fought off the zombies successfully!")
            self.location = "treasure_hunt"
        else:
            print("You and your friend(s) were overwhelmed by the zombies.")
            self.alive = False

    def treasure_hunt_scene(self):
        print("You've found a treasure chest, but it's locked with a riddle...")
        if self.clue:
            print("The clue you found says: 'It's an instrument that can't unlock anything.'")
        riddle_answer = input("What has keys but can't open locks? ")

        if riddle_answer.lower() == "piano":
            print("You've solved the riddle and opened the treasure chest!")
            self.has_treasure = True
        else:
            print("You couldn't solve the riddle and the treasure chest remains locked...")
            self.alive = False

game = Game()
game.start()

#The End