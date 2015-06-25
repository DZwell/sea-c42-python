import sys

while True:

    def send_thanks():
        print("To see a list of donors, type 'list'. Otherwise, enter a donor name.")
        answer2 = input('> ')
        if (answer2 == 'list' or answer2 == 'List'):
            print(donor_list)
        elif (answer2 == 'q' or answer2 == 'Q'):
            prompt_user()

    def prompt_user():
        print("What would you like to do?\nSend (T)hank You \nCreate (R)eport\n(Q)uit")
        answer1 = input('> ')
        if (answer1 == "q" or answer1 == "Q"):
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

