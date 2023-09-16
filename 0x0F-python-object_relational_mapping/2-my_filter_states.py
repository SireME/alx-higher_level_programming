#!/usr/bin/python3
"""
this script  lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    def list_states_by_name(un, pwd, db_nm, state_name):
        """
        get all row with specific input state, takes in state
        as 4th argument
        note: table created from .sql script of similar name
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
        sn = state_name
        cc.execute("SELECT * FROM states WHERE name = '{:s}'\
                ORDER By id ASC;".format(sn))
        results = cc.fetchall()
        # display of exectution result
        for row in results:
            print(row)

        # close cursor and database
        cc.close()
        db.close()

    # execute code list all states in db
    import MySQLdb
    from sys import argv
    list_states_by_name(argv[1], argv[2], argv[3], argv[4])
