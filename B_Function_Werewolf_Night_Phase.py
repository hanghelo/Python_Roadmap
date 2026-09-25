import time
dot = "..."
everyone = "Everyone, close your eyes "
werewolves = "Werewolves, wake up "
hunter = "Hunter, wake up "
seer = "Seer, wake up "
bodyguard = "Bodyguard, wake up "

def function_dotprinting():
    for eachdot in dot:
        print (eachdot, end="", flush=True)     #flush forces to display every dot   
        time.sleep (1)


def night_phase ():
    print (everyone, end="")
    function_dotprinting ()
    time.sleep(0.5)  # Pauses the script for 0.5 seconds
    print ()

    print (hunter, end="")
    function_dotprinting ()
    time.sleep(0.5)  # Pauses the script for 0.5 seconds
    print ()

    print (seer, end="")
    function_dotprinting ()
    time.sleep(0.5)  # Pauses the script for 0.5 seconds
    print ()

    print (bodyguard, end="")
    function_dotprinting ()
    time.sleep(0.5)  # Pauses the script for 0.5 seconds

# night_phase () - No need to declare because of the if _name_ == "_main_" --- as the system will check if the code runs from the direct file or from an imported file.


# This line of code prevents the code inside it from automatically running when the file is imported by another Python file. Note that the # the function_dotprinting() function is inside the nigh_phase() function

# Therefore,
# Directly run the file → execute it all.
# Import the file → don't execute the main part (the night phase() function).

# If this file/function/code is directly executed from this main file ..
if __name__ == "__main__":
    night_phase() 