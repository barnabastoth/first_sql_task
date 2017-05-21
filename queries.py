import psycopg2


def info_from_database(func):
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


def update_database(func):
    def wrap():
        connect_str = "dbname='exworm' user='exworm' host='localhost' password='fanatic99'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(func())
    return wrap


@info_from_database
def mentor_names():
    return """SELECT first_name,last_name FROM mentors;"""


@info_from_database
def mikolc_mentor_nicknames():
    return """SELECT nick_name FROM mentors WHERE city='Miskolc';"""


@info_from_database
def carol_information():
    return """SELECT first_name, last_name, phone_number FROM applicants WHERE first_name = 'Carol';"""


@info_from_database
def girl_from_adipiscingenimmi():
    return """SELECT first_name, last_name, phone_number FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu%';"""


@info_from_database
def check_for_markus():
    return """SELECT exists(SELECT application_code FROM applicants WHERE application_code = 54823)"""


@update_database
def new_applicant_markus():
    show_applicant_markus()
    return """INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
            SELECT 'Markus', 'Schaffarzyk', '003620/725-2666','djnovus@groovecoverage.com', 54823
            WHERE NOT EXISTS (SELECT * FROM applicants WHERE application_code=54823);"""


@info_from_database
def show_applicant_markus():
    return """SELECT * FROM applicants WHERE application_code=54823;"""


@update_database
def update_jemima_foreman():
    show_jemima_foreman()
    return """UPDATE applicants SET phone_number = '003670/223-7459'
           WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""


@info_from_database
def show_jemima_foreman():
    return """SELECT phone_number FROM applicants WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""


@update_database
def delete_mauriseu():
    return """DELETE FROM applicants WHERE email LIKE '%@mauriseu.net%';"""
