#!/usr/bin/python

import psycopg2
from config import config



def insert_checked_devices(**checked_devices):

    """ insert devices into the checked_devices table  """
    sql = """INSERT INTO checked_devices(
                hostname,
                management_ip,
                serial
                ) VALUES (
                %(hostname)s, 
                %(management_ip)s, 
                %(serial)s
                )"""
    

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, checked_devices)
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
    insert_checked_devices(
            hostname = "vios4",
            management_ip = "10.60.0.4",
            serial = "9P7OJVD6W13"
            )