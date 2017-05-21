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
    allowed_inputs = [_ for _ in range(1, len(options) + 1)]
    menu.sql_menu(options, allowed_inputs)


if __name__ == '__main__':
    main()
