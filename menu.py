import os


def sql_menu(options, allowed_inputs, menu_options):
    for option in menu_options:
        print(option)
    incorrect_input = True
    while incorrect_input:
        try:
            chosen_option = int(input("Enter a number between 1 and {0}: ".format(len(allowed_inputs))))
            if chosen_option in allowed_inputs:
                if chosen_option == 7:
                    os.system('clear')
                    for option in menu_options:
                        print(option)
                    print("\n" + "Result of your query is: " + "\n")
                    print("Applicant with email @mauriseu.net has been removed from the database")
                    options[chosen_option]()

                else:
                    os.system('clear')
                    for option in menu_options:
                        print(option)
                    print("\n" + "Result of your query is: " + "\n")
                    options[chosen_option]()
            elif chosen_option == 0:
                incorrect_input = False
            else:
                print("Incorrect input! Valid inputs are: 1, 2, 3, 4, 5, 6, 7, 8, 9")
        except ValueError:
            print("Incorrect input! Valid inputs are: 1, 2, 3, 4, 5, 6, 7, 8, 9")
