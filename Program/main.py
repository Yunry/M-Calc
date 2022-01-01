import sys


def interface():
    print(""" __       __           ______             __                      __              __                         
/  \     /  |         /      \           /  |                    /  |            /  |                        
$$  \   /$$ |        /$$$$$$  |  ______  $$ |  _______  __    __ $$ |  ______   _$$ |_     ______    ______  
$$$  \ /$$$ | ______ $$ |  $$/  /      \ $$ | /       |/  |  /  |$$ | /      \ / $$   |   /      \  /      \ 
$$$$  /$$$$ |/      |$$ |       $$$$$$  |$$ |/$$$$$$$/ $$ |  $$ |$$ | $$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |
$$ $$ $$/$$ |$$$$$$/ $$ |   __  /    $$ |$$ |$$ |      $$ |  $$ |$$ | /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ 
$$ |$$$/ $$ |        $$ \__/  |/$$$$$$$ |$$ |$$ \_____ $$ \__$$ |$$ |/$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      
$$ | $/  $$ |        $$    $$/ $$    $$ |$$ |$$       |$$    $$/ $$ |$$    $$ |  $$  $$/ $$    $$/ $$ |      
$$/      $$/          $$$$$$/   $$$$$$$/ $$/  $$$$$$$/  $$$$$$/  $$/  $$$$$$$/    $$$$/   $$$$$$/  $$/       
                                                                                                             
                                                                                                             
                                                                                                             v.0.1""")
    try:
        choice()
    except ValueError:
        print("Please enter a valid number as a choice.\n")
        choice()


def show_options():
    print("MENU\n")
    print("Press the number to enter the option")
    print("0. Information & Usage (menu)")
    print("1. Mortgage Calculator ")
    print("2. Custom Subscription Calculator")
    print("3. Savings")
    print("4. About the program")
    print("Enter 'q' to exit")


def choice():
    show_options()
    menu_choice = input()

    if menu_choice == "q":
        sys.exit("User has terminated the program")
    else:
        while int(menu_choice) not in range(0, 5):
            show_options()
            menu_choice = input()


# Shows the menu at the start
try:
    interface()
except KeyboardInterrupt:
    print("\nThe User has terminated the program via keyboard.")
