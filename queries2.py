import psycopg2


def user_datas():
    """Read the nessecery information from the user_file to
    connect to the database, such as dbname, username, password
    """
    with open('user.txt') as file:
        data = file.read()
        data = data.split(',')
        return data


def fetch_database(query, tuple_parameters=None):
    """Connects to the database to retrieve data, then
    returns it.
    """
    try:
        data = user_datas()
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query, tuple_parameters)
        rows = cursor.fetchall()
        return rows

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if conn:
            conn.close()


def mentors_and_schools():
    return fetch_database("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS name, schools.name, schools.country
                          FROM mentors LEFT JOIN schools ON mentors.city = schools.city ORDER BY mentors.ID""")


def mentors_and_schools_all():
    return fetch_database("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS name, schools.name, schools.country
                          FROM mentors FULL OUTER JOIN schools ON mentors.city = schools.city ORDER BY mentors.ID""")


def mentors_by_country():
    return fetch_database("""SELECT country, COUNT(last_name) AS numpercountry
                          FROM mentors JOIN schools ON mentors.city = schools.city""")
