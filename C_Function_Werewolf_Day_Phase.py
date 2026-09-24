from B_Function_Werewolf_Night_Phase import function_dotprinting

night_over = "Night is over "
all_wakeup = "Everyone wakes up "
nights_result = "The Moderator announces the night's results "
discussion = "Players discuss "
voting = "Players vote "

def day_phase():
    print (night_over, end="")
    function_dotprinting()
    print ()

    print (all_wakeup, end="")
    function_dotprinting()
    print ()

    print (nights_result, end="")
    function_dotprinting()
    print ()

    print (discussion, end="")
    function_dotprinting()
    print ()

    print (voting, end="")
    function_dotprinting()
    print ()

if __name__ == "__main__":
    day_phase()