#!/usr/bin/python3
"""
this script  lists all cities by sate
from the database hbtn_0e_4_usa
main target: joins
use only single execute statement
"""


if __name__ == "__main__":
    def list_cities_by_state(un, pwd, db_nm, state):
        """
        print all cities from a specific state
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
        WHERE states.name = %s
        ORDER By cities.id;
        """, (state,))

        # display of exectution result
        cities = ", ".join([i[1] for i in cc.fetchall()])
        print(cities)

        # close cursor and database
        cc.close()
        db.close()

    # execute code list all states, cities
    import MySQLdb
    from sys import argv
    list_cities_by_state(argv[1], argv[2], argv[3], argv[4])
