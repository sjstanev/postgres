#!/usr/bin/python

import psycopg2
from config import config


def insert_device_info(**device_info):

    """ insert devices into the checked_devices table  """
    sql = """INSERT INTO device_info(
                hostname,
                uptime,
                version,
                software_image,
                hardware,
                serial,                
                management_ip,
                management_intif                
                )                 
                VALUES (
                    %(hostname)s, 
                    %(uptime)s, 
                    %(version)s, 
                    %(software_image)s, 
                    %(hardware)s, 
                    %(serial)s, 
                    %(management_ip)s, 
                    %(management_intif)s
                    )
        """


    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, device_info)
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

    # insert common information into device_info
    insert_device_info(
            hostname = "null",
            uptime = "null",
            version = "null",
            software_image = "null",
            hardware = "null",
            serial = "null",
            management_ip = "null",
            management_intif = "null"
            )