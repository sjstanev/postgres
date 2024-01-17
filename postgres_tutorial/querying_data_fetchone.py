#!/usr/bin/python

"""
The  fetchone() fetches the next row in the result set. It returns a single tuple or None when no more row is available.
"""

import psycopg2
from config import config


def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
         # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
        print(f' ----- {row}------',type(row))
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_vendors()