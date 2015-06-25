import sys


donor_list = [['Frank Zappa'], ['Geroge Benson'], ['Zorro'], ['Vito Corleone']]


while True:

    def send_thanks():
        print("Please enter a name, or choose from the following:\n"
            "list - Print a list of previous donors\n"
            "quit - Return to main menu")
        answer2 = input('> ')
        if (answer2 == 'list' or answer2 == 'List'):
            print(donor_list[:])
            send_thanks()
        elif (answer2 == 'quit' or answer2 == 'Quit'):
            prompt_user()
        else:
            print("")

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






    # if (user input == 'q'):
    #     def Quit script():

    # prompt = answer
    #     if (user input == 'q'):
    #         def Quit prompt():

    #     if (prompt == send thankyou):
    #         if (user asks to see list):
    #             def show list of donor names, reprompt():

    #         if (name typed in doesn't exist):
    #             def add name to [],():

    #         elif (name exists):
    #             def prompt for donation amount():

    #             if (donation is number):
    #                 add amount to donation history
    #                 print("Thank you %s for your donation of $ %d ")
    #                 Back to original prompt
    #             else:
    #                 reprompt
    #     else:
    #         if (user input == 'q'):
    #         def Quit prompt():

    #         print list of donors sorted by total historical donation amount
    #             list = [donor name, total donated,
    #             number of donations, avg donation amount]

    #             print in nice rows and columns
    #             Back to original prompt

