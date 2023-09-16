#!/usr/bin/python3
"""
this script  lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    def list_all_states(un, pwd, db_nm):
        """
        get all rows from specific table
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
        cc.execute("""
        SELECT *
        FROM states
        ORDER By states.id;
        """)

        # display of exectution result
        for row in cc.fetchall():
            print(row)

        # close cursor and database
        cc.close()
        db.close()

    # execute code list all states in db
    import MySQLdb
    from sys import argv
    list_all_states(argv[1], argv[2], argv[3])
