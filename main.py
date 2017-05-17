import psycopg2
from psycopg2 import IntegrityError
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
def check_for_markus():
    return """SELECT exists(SELECT application_code FROM applicants WHERE application_code = 54823)"""


def new_applicant_markus():
    connect_str = "dbname='exworm' user='exworm' host='localhost' password='fanatic99'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
            SELECT 'Markus', 'Schaffarzyk', '003620/725-2666','djnovus@groovecoverage.com', 54823
            WHERE NOT EXISTS (SELECT * FROM applicants WHERE application_code=54823);""")
    show_applicant_markus()


@open_database
def show_applicant_markus():
    return """SELECT * FROM applicants WHERE application_code=54823;"""


def update_jemima_foreman():
    connect_str = "dbname='exworm' user='exworm' host='localhost' password='fanatic99'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("""UPDATE applicants SET phone_number = '003670/223-7459'
           WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    show_jemima_foreman()


@open_database
def show_jemima_foreman():
    return """SELECT phone_number FROM applicants WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""


@open_database
def delete_mauriseu():
    return """DELETE FROM applicants WHERE email LIKE '%@mauriseu.net%';"""


def main():
    options = {
        1: mentor_names,
        2: mikolc_mentor_nicknames,
        3: carol_full_name,
        4: girl_from_adipiscingenimmi,
        5: new_applicant_markus,
        6: update_jemima_foreman,
        7: delete_mauriseu
    }
    allowed_inputs = [_ for _ in range(1, len(options) + 1)]
    menu.sql_menu(options, allowed_inputs)


if __name__ == '__main__':
    main()
