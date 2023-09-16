#!/usr/bin/env python3
"""
this script  lists all states from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    def list_all_states(un, pwd, db_nm):
        """
        get all rows from specific table
        note: table created from .sql script of similar name
        """
        db = MySQLdb.connect(user=un, password=pwd, database=db_nm, port=3306)
        cc = db.cursor()
        cc.execute("""
        SELECT *
        FROM states;
        """)
        for row in cc.fetchall():
            print(row)
        cc.close()
        db.close()

    # execute code list all states in db
    import MySQLdb
    from sys import argv
    list_all_states(argv[1], argv[2], argv[3])
