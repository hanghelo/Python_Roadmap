import time
werewolf_roles = [
    "• 🏹 Hunter",
    "• 🔮 Seer",
    "• 🛡️ Bodyguard",
    "• 👨‍🌾 Villager",
    """• 🐺 Werewolf 
    • 5–6 players → maximum 1
    • 7+ players → maximum 2"""
]

game_objective = """Villagers: Identify and eliminate all Werewolves before the Werewolves take control.

Werewolves: Eliminate enough Villagers to gain control of the village without being discovered.

Moderator: Manage the game, reveal information when needed, and keep track of all players, roles, and actions."""

moderator_reminder = """🎭 Moderator Reminder

Keep all roles and secret actions confidential. Guide each phase, track player status, and ensure everyone follows the rules."""

def start_game():
    # Game title
    print ("--- Welcome to the ---")
    print ("THE ULTIMATE WEREWOLF GAME")
    print ()
    time.sleep(2)  # Pauses the script for 2 seconds

    # Minimum number of players
    print ("-------------------------------------------------------------")
    print ("Note: To start the game, you should have atleast 5 players.")
    print ()
    time.sleep(0.5)  # Pauses the script for 0.5 second

    # Required roles
    print ("-------------------------------------------------------------")
    print ("Min Required Roles:")
    for each_role in werewolf_roles:
        print (each_role)
    print ()
    time.sleep(0.5)  # Pauses the script for 0.5 second

    # Basic objective
    print ("-------------------------------------------------------------")
    print ("Game Objectives:")
    print (game_objective)
    time.sleep(0.5)  # Pauses the script for 0.5 second
    print ()

    # Moderator reminder
    print ("-------------------------------------------------------------")
    print ("Moderator Reminder")
    print (moderator_reminder)

start_game()