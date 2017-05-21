def sql_menu(options, allowed_inputs):
    print("Choose from one of the following options: ")
    print("0: Exit")
    print("1: Full name of all the mentors")
    print("2: Nick names of the mentors at Miskolc")
    print("3: Full name of Carol the applicant")
    print("4: Full name of Applicant from Adipiscingenimmi")
    print("5: Add Markus Schaffarzyk to the Applicants")
    print("6: Update phone number of Jemina Foreman")
    print("7: Delete Applicants with @mauriseu.net email adress ending")
    incorrect_input = True
    while incorrect_input:
        try:
            chosen_option = int(input("Enter a number between 1 and {0}: ".format(len(allowed_inputs))))
            if chosen_option in allowed_inputs:
                options[chosen_option]()
            elif chosen_option == 0:
                incorrect_input = False
            else:
                print("Incorrect input! Valid inputs are: 1, 2, 3, 4, 5, 6, 7, 8, 9")
        except ValueError:
            print("Incorrect input! Valid inputs are: 1, 2, 3, 4, 5, 6, 7, 8, 9")
