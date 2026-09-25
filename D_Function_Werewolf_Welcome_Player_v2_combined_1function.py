player_names = []

roles_for_5players = [
    "- 🏹 Hunter",
    "- 🔮 Seer",
    "- 🛡️ Bodyguard",
    "- 👨‍🌾 Villager",
    "- 🐺 Werewolf"
]

roles_for_6players = [
    "- 🏹 Hunter",
    "- 🔮 Seer",
    "- 🛡️ Bodyguard",
    "- 👨‍🌾 Villager",
    "- 👨‍🌾 Villager",
    "- 🐺 Werewolf"
]

roles_for_7players = [
    "- 🏹 Hunter",
    "- 🔮 Seer",
    "- 🛡️ Bodyguard",
    "- 👨‍🌾 Villager",
    "- 👨‍🌾 Villager",
    "- 🐺 Werewolf",
    "- 🐺 Werewolf"
]

##############################################################################3
# Checking the player count

def check_player_count(player_count) :
    if player_count < 5:
        print ("❌ Not enough players. Get 5 players to start the game")

    elif player_count >=5 and player_count <=7:
        print (f"Entering to the game with {player_count} players...")
        print ("Playing with ...")

        if player_count == 5:
            print (f"{player_count-1} villagers : 1 werewolf")
            print ("Available Roles:")

            for everyroles in roles_for_5players:
                print (everyroles)

        elif player_count == 6:
            print (f"{player_count-1} villagers : 1 werewolf")
            print ("Available Roles:")

            for everyroles in roles_for_6players:
                print (everyroles)

        else:
            print (f"{player_count-2} villagers : 2 werewolf")
            print ("Available Roles:")

            for everyroles in roles_for_7players:
                print (everyroles)


    else:
        print ("❌ Not supported yet. 8+ cannot be played yet")


while True:
    try:
        input_checkplayercount = int(input("Enter player count: "))
        check_player_count (input_checkplayercount)

    except ValueError:
        print("Oops! That was not a valid number.")