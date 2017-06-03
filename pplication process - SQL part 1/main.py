import menu
import queries


def main():
    options = {
        1: queries.mentor_names,
        2: queries.mikolc_mentor_nicknames,
        3: queries.carol_information,
        4: queries.girl_from_adipiscingenimmi,
        5: queries.new_applicant_markus,
        6: queries.update_jemima_foreman,
        7: queries.delete_mauriseu
    }
    menu_options = [
        "Choose from one of the following options: ",
        "0: Exit",
        "1: Full name of all the mentors",
        "2: Nick names of the mentors at Miskolc",
        "3: Full name of Carol the applicant",
        "4: Full name of Applicant from Adipiscingenimmi",
        "5: Add Markus Schaffarzyk to the Applicants",
        "6: Update phone number of Jemina Foreman",
        "7: Delete Applicants with @mauriseu.net email adress ending"
    ]
    allowed_inputs = [_ for _ in range(1, len(options) + 1)]
    menu.sql_menu(options, allowed_inputs, menu_options)


if __name__ == '__main__':
    main()
