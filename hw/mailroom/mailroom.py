import sys


donor_list = ['Frank Zappa', 'Geroge Benson', 'Zorro', 'Vito Corleone']


while True:

    def send_thanks():
        print("Please enter a name, or choose from the following:\n"
            "list - Print a list of previous donors\n"
            "quit - Return to main menu")
        answer2 = input('> ')
        if (answer2 == 'list' or answer2 == 'List'):
            print(donor_list[::])
            send_thanks()
        elif (answer2 == 'quit' or answer2 == 'Quit'):
            prompt_user()
        else:
            if (answer2 in donor_list):
                print("Enter a donation amount or 'quit:")
                donation_amount = input('> ')
                print("Dear %s,\n\n"
                    "Thank you so much for your generous donatation of $%d. "
                    "\nWe here at 'Dogs Are People Too' couldn't succed in "
                    "advocating for human rights for dogs "
                    "\nwith out people like you. With election season coming up, "
                    "your money will go towards a new piece of legislation "
                    "desinged to give dogs access to free public education.\n"
                    "\nThank you again,\n\nDaniel Zwelling\n\nPresident, D.A.P.T\n\n "
                    % (answer2, int(donation_amount)))

    def prompt_user():
        print("Welcome to Mailroom Madness\nChoose from the following:\n"
            "T - Send a (T)hank You \nR - Create (R)eport\n"
            "quit - Quit the program")
        answer1 = input('> ')
        if (answer1 == "quit" or answer1 == "Quit"):
            sys.exit()
        elif (answer1 == "t" or answer1 == "T"):
            send_thanks()

    prompt_user()



