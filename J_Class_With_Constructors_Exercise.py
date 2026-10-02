
class Character:
    def __init__(self, name, hp, mp, atk, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.lvl = lvl
        print (name + " - Character Created")

hanabi = Character ("Hanabi", 100, 50, 12, 1)
change = Character ("Change", 120, 40, 20, 5)

print (change.name +" "+ str(change.atk))
