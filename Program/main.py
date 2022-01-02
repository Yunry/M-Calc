import sys
from decimal import Decimal


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
        interface()


def show_options():
    print("\n#####MENU#####")
    print("Press the number to enter the option")
    print("0. Information & Usage (menu)")
    print("1. Mortgage Calculator ")
    print("2. About the project")
    print("Enter 'q' to exit")
    print("#####MENU#####\n")


def choice():
    show_options()
    menu_choice = input("Enter here: ")

    while menu_choice != "q":
        while int(menu_choice) not in range(0, 5):
            show_options()
            menu_choice = input("Enter here: ")

        # execution of choices
        switch(int(menu_choice))
    sys.exit("User has terminated the program")


# switch-case simulation (just for fun)
def switch(num):
    if num == 0:
        option_zero()
        choice()
    elif num == 1:
        option_one()
        choice()
    elif num == 2:
        option_two()
        choice()
    else:
        print("\nOops, something went wrong...\nRestarting the application...")
        choice()


# different options
def option_zero():
    print("#####INFORMATION#####")
    print("This is a very simple program for calculating mortgages and more. Use numbers corresponding to order to "
          "navigate.")
    print("#####INFORMATION#####")


def option_one():
    print("#####OPTION: MORTGAGE CALCULATOR#####")
    # TODO later: make default values for calculation
    # needed user input variables for formula
    a_r, N, P = first_input()
    r = a_r / 100 / 12
    result = (r * P * (1 + r) ** N) / ((1 + r) ** N - 1)
    if fixed_or_adjustable():
        print("\nMonthly payment for a fixed rate mortgage -- standard calculation used in the US")
        print(
            "The amount paid by the borrower every month that ensures that the loan is paid off in full with interest "
            "at the end of its term. The monthly payment formula is based on the annuity formula\n")
        if r == 0:
            print(f"Your monthly payments will amount to(since there is no interest): ${P / N}")
        else:
            print(f"Your monthly payments will amount to: ${round(result, 2)}")
    else:
        month_before_adjustment = int(input("Please input the number of month before adjustments(standard: 60): "))
        month_between_adjustment = int(input("Please enter the month between the adjustments(standard(12): "))
        expected_adj = float(input("Please enter the expected adjustment(standard: 0.25): "))
        interest_cap = float(input("Please enter the interest rate cap(standard: 12): "))

        a_result = 0
        for i in range(0, int(N + 1)):
            if i <= month_before_adjustment:
                a_result = result
            else:
                if a_r < interest_cap and i % month_between_adjustment == 0:
                    a_r += expected_adj
                if a_r == float(interest_cap):
                    a_r = a_r / 100 / month_between_adjustment
                    a_result = (a_r * P * (1 + a_r) ** N) / ((1 + a_r) ** N - 1)
                    break
        print(
            f"Your adjustable rate loan of ${round(P, 2)} for {int(N / 12)} years has a starting payment of ${round(result, 2)}. \nYour interest rate remains fixed at {round(r * 100 * 12, 2)}% for {month_before_adjustment} months, after that time your interest "
            f"rate is expected to change by {expected_adj}% every {month_between_adjustment} months. \nYour highest "
            f"monthly payment, "
            f"in this scenario, would be ${round(a_result, 2)}")

        # the adjustment calculation may be wrong --> differs from online


# method for determining which formula should be used
def fixed_or_adjustable():
    answer = int(input("Is your mortgage fixed or adjustable?\nPlease enter '0' for fixed and '1' for adjustable: "))
    if answer == 0:
        return True
    else:
        return False


def first_input():
    try:
        a_r = float(input("Yearly interest rate: "))  # monthly interest rate
        N = float(input("Number of years for payment --> Loan's term: ")) * 12  # number of monthly payments
        P = float(input("Amount borrowed(in USD) --> Loan's principal: "))
        return a_r, N, P
    except ValueError:
        print("Incorrect input. Please enter again.")
        first_input()


def option_two():
    print("\nWhy this project?")
    print("It is a starting project of mine for diving into Python and exploring its possibilities.\nI just found "
          "this project idea in my Codecademy Course and thought this would be a great starting project as it also "
          "has some real-life appliance.\nIf you have found some kind of bugs, issues or update ideas...feel free to "
          "notify me about them")


# Shows the menu at the start
try:
    interface()
except KeyboardInterrupt:
    sys.exit("User has terminated the program")
