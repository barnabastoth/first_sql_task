import psycopg2
import menu


def open_database(func):
    def wrap():
        connect_str = "dbname='exworm' user='exworm' host='localhost' password='fanatic99'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(func())
        rows = cursor.fetchall()
        for row in rows:
            print(" ".join(map(str, row)))
    return wrap


@open_database
def mentor_names():
    return """SELECT first_name,last_name FROM mentors;"""


@open_database
def mikolc_mentor_nicknames():
    return """SELECT nick_name FROM mentors WHERE city='Miskolc';"""


@open_database
def carol_full_name():
    return """SELECT first_name, last_name FROM applicants WHERE first_name = 'Carol';"""


@open_database
def girl_from_adipiscingenimmi():
    return """SELECT first_name, last_name FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu%';"""


@open_database
def new_applicant_markus():
    return """INSERT INTO applicants(first_name,last_name,phone_number,email,application_code)
            VALUES ('Markus', 'Schaffarzyk', '003620/725-2666','djnovus@groovecoverage.com', 54823);"""


@open_database
def show_applicant_markus():
    return """SELECT * FROM applicants WHERE application_code=54823;"""


@open_database
def update_jemima_foreman():
    return """UPDATE applicants SET phone_number = '003670/223-7459'
           WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""


@open_database
def show_jemima_foreman():
    return """SELECT phone_number FROM applicants WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""


@open_database
def delete_mauriseu():
    return """DELETE FROM applicants WHERE email LIKE '%@mauriseu.net%';"""


def main():
    allowed_inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    options = {
        1: mentor_names,
        2: mikolc_mentor_nicknames,
        3: carol_full_name,
        4: girl_from_adipiscingenimmi,
        5: new_applicant_markus,
        6: show_applicant_markus,
        7: update_jemima_foreman,
        8: show_jemima_foreman,
        9: delete_mauriseu
    }
    menu.sql_menu(options, allowed_inputs)


if __name__ == '__main__':
    main()
