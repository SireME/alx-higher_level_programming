#!/usr/bin/python3
"""
this script  lists all states from the database hbtn_0e_4_usa
main taget joins
use only single execute
"""


if __name__ == "__main__":
    def list_all_states_cities(un, pwd, db_nm):
        """
        get rows from cities and states table via join
        and print neccesary data (id, city, state)
        """
        # keyword arguments for connect
        karg = {"host": "localhost", "user": un, "password": pwd}
        karg["database"] = db_nm
        karg["port"] = 3306
        karg["charset"] = "utf8"

        # connection to db
        db = MySQLdb.connect(**karg)

        # cursor creation
        cc = db.cursor()

        # command execution
        cc.execute("""
        SELECT cities.id, cities.name, states.name
        FROM states JOIN cities
        ON states.id = cities.state_id
        ORDER By cities.id;
        """)

        # display of exectution result
        for row in cc.fetchall():
            print(row)

        # close cursor and database
        cc.close()
        db.close()

    # execute code list all states, cities
    import MySQLdb
    from sys import argv
    list_all_states_cities(argv[1], argv[2], argv[3])
