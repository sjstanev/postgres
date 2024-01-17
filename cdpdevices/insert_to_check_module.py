#!/usr/bin/python

import psycopg2
from config import config



def to_check_device(**to_check):

    """ insert devices into the checked_devices table  """
    sql = """INSERT INTO to_check(
                hostname,
                management_ip,
                flag
                ) VALUES (
                %(hostname)s, 
                %(management_ip)s, 
                %(flag)s)"""
    

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, to_check)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':

    # insert cdp neighbours parameters into cdpneighbor table
    to_check_device(
            hostname = "vios4",
            management_ip = "10.60.0.4",
            flag = "Null"
            )