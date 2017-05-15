import psycopg2
import queries


def open_database(func):
    def wrap():
        connect_str = "dbname='exworm' user='exworm' host='localhost' password='fanatic99'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(func())
        rows = cursor.fetchall()
        if func() == mentor_names:
            for row in rows:
                print("Menthor: ")
                print('First Name: {0} Last Name: {1}'.format(row[0], row[1]))
        else:
            print("asd")
    return wrap


@open_database
def mentor_names():
    return """SELECT first_name,last_name FROM mentors;"""


def main():
    mentor_names()


if __name__ == '__main__':
    main()
