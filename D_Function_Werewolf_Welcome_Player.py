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

        # Return False, inform the systems that condition is FALSE and NOT MET, and the FALSE output can be used because of the return statement
        return False

    elif player_count <= 7:
        print (f"Entering to the game with {player_count} players...")

        # Return True, inform the systems that condition is TRUE and MET, and the TRUE output can be used because of the return statement
        return True

    else:
        print ("❌ Not supported yet. 8+ cannot be played yet")

        # Return False, inform the systems that condition is FALSE and NOT MET, and the FALSE output can be used because of the return statement
        return False

input_checkplayercount = int(input("Enter player count: "))
check_player_count (input_checkplayercount)

##############################################################################3
# Checking the number of wolves

def wolf_counter (player_count) :
    print ("Playing with ...")
    if player_count < 5:
        print ("❌ Not enough players. Get 5 players to start the game")

    elif player_count >= 5 and player_count <=6:
        print (f"{player_count-1} villagers : 1 werewolf")

        # Return 1 wolf
        wolf = 1
        return wolf

    elif player_count == 7:
        print (f"{player_count-2} villagers : 2 werewolves")
        
        # Return 1 wolf
        wolf = 2
        return wolf

    else:
        print (f"{player_count} player(s) is not supported yet.")

wolf_counter (input_checkplayercount)

##############################################################################3
# Display the correct roles

def role_config (player_count) :
    print ("Available Roles:")
    if player_count < 5:
        print ("❌ Not enough players. Get 5 players to start the game")

    elif player_count == 5:
        print (roles_for_5players)

    elif player_count == 6:
        print (roles_for_6players)

    elif player_count == 7:
        print (roles_for_7players)

    else:
        print (f"{player_count} player(s) is not supported yet.")

role_config (input_checkplayercount)