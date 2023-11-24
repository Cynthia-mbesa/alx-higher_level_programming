#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#
import sys
import MySQLdb

if __name__ == "__main__":
    # connect to mysql database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # create a cursor object to interact with database
    c = db.cursor()
    # execute the sql querry
    c.execute("SELECT * FROM `states`")
    # print each state fetched from database
    [print(state) for state in c.fetchall()]
