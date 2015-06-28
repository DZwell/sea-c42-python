import sys


donor_list = [['Frank Zappa', 4, 2, 180], ['George Benson', 18, 36, 72],
['Zorro', 25, 200, 13], ['Vito Corleone', 5000, 1500, 2500],
['Hank Hill', 100, 300, 75]]


while True:

    def send_thanks():
        print("Please enter a name, or choose from the following:\n"
            "list - Print a list of previous donors\n"
            "quit - Return to main menu")
        send_thanks.answer2 = input('> ')
        if (send_thanks.answer2 == 'list' or send_thanks.answer2 == 'List'):
            print(donor_list[::])
            print("\n")
            send_thanks()
        elif (send_thanks.answer2 == 'quit' or send_thanks.answer2 == 'Quit'):
            prompt_user()
        else:
            for i in donor_list:
                if (send_thanks.answer2 in i):
                    write_letter()
                if (send_thanks.answer2 not in i):
                    new_donor() # keeps calling this even when first if is True

    def write_letter():
        print("Enter a donation amount or 'quit:")
        donation_amount = input('> $')
        donor_list[4].append(donation_amount) #Append to [i]
        # if (donation_amount.isdigit() == False):
        #     print("Please enter a number")
        print("Dear %s,\n\n"
            "Thank you so much for your generous donatation of $%d. "
            "\nWe here at 'Dogs Are People Too' couldn't succed in "
            "advocating for human rights for dogs "
            "\nwithout people like you. With election season coming up, "
            "your money will go towards a new piece of legislation "
            "designed to give dogs access to free public education.\n"
            "\nThank you again,\n\nDaniel Zwelling\n\nPresident, D.A.P.T\n\n "
            % (send_thanks.answer2, int(donation_amount)))

        send_thanks()

    def new_donor():
        donor_list.append([send_thanks.answer2])
        write_letter()

    def prompt_user():
        print("\nWelcome to Mailroom Madness\nChoose from the following:\n"
            "T - Send a (T)hank You \nR - Create (R)eport\n"
            "quit - Quit the program")
        answer1 = input('> ')
        if (answer1 == "quit" or answer1 == "Quit"):
            sys.exit()
        elif (answer1 == "t" or answer1 == "T"):
            send_thanks()
        elif (answer1 == "r" or answer1 == "R"):
            create_report()

    def create_report():
        print('Name   | Total | # | Average\n\n' + ('_' * 50))


    prompt_user()








