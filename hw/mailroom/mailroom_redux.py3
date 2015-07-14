import sys

donor_list = {
    'Frank Zappa': [4, 2, 180],
    'George Benson': [18, 36, 72],
    'Al Capone': [25, 200, 13],
    'Vito Corleone': [5000, 1500, 2500],
    'Hank Hill': [100, 300, 75]}


def create_report():
    print('Name\t\t|\tTotal\t|\t#\t|\tAverage\n\n' + ('_' * 50))
    sorted_list = sorted(donor_list, key=lambda donor: sum(donor_list[donor]), reverse=True)
    for akey in sorted_list:
        donor_name = akey
        total = sum(donor_list[akey])
        number = len(donor_list[akey])
        average = total / number
        print('%s\t|\t$%d\t|\t%d\t|\t$%d' %
        (donor_name, total, number, average))


# itterates through dict and prints keys(donor names)
def donor_names():
    for key in donor_list:
        print(key, '\n')


def append_donation(donor, dollars):
    donor_list[donor].append(dollars)


def new_donor(donor, dollars):
    # Adds new key/value pair to dictionary. [] makes value a list.
    donor_list[donor] = [dollars]


def write_thanks(donor, dollars):
    letter = ("Dear %s,\n\n"
            "Thank you so much for your generous donatation of $%d. "
            "\nWe here at 'Dogs Are People Too' couldn't succed in "
            "advocating for human rights for dogs "
            "\nwithout people like you. With election season coming up, "
            "your money will go towards a new piece of  legislation "
            "designed to give dogs access to free public education.\n"
            "\nThank you again,\n\nDaniel Zwelling\n\nPresident, D.A.P.T\n\n "
            % (donor, dollars))

    #  creates file called donor.txt with 'write' capabilities. within this scope, called f.
    with open(donor + '.txt', 'w') as f:
        f.write(letter)
    print(letter)


if __name__ == '__main__':

    while True:
        user_choice = input("\nWelcome to Mailroom Madness\nChoose from the following:\n"
                    "T - Send a (T)hank You \nR - Create (R)eport\n"
                    "quit - Quit the program\n> ")

        while True:
            if user_choice == 'R' or user_choice == 'r':
                create_report()
                break

            elif user_choice == 'T' or user_choice == 't':
                name = input("Please enter a name, or choose from the following:\n"
                    "list - Print a list of previous donors\n"
                    "quit - Return to main menu\n> ")

                if name == 'quit':
                    break

                elif name == 'list':
                    donor_names()

                else:
                    try:
                        amount = int(input('Please enter donation amount\n$ '))
                    except ValueError:
                        print('Invalid input, please enter a number')

                    donor = False
                    for key in donor_list:
                        if name == key:
                            donor = True
                            break
                        else:
                            donor = False

                    if donor == True:
                        append_donation(name, amount)

                    else:
                        new_donor(name, amount)

                    write_thanks(name, amount)
                    break

            elif user_choice == 'quit':
                sys.exit()
                break

            else:
                mode = input("Invalid input. Please enter 'R', 'T' or 'quit'")





