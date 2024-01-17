#!/usr/bin/python

import psycopg2
from config import config



def insert_cdpneihbor(cdp_neighors_param):
    """ insert multiple cdpneighbors into the vendors table  """
    sql = """INSERT INTO cdpneighbors(
                local_host,
                destination_host,
                management_ip,
                platform, 
                remote_port, 
                local_port, 
                software_version,
                capabilities) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,cdp_neighors_param)
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

    device = {"hostname": "vios3","destination_host": "RB4011iGS",
    "management_ip": "10.60.0.1",
    "platform": "MikroTik2",
    "remote_port": "MANAGEMENT",
    "local_port": "GigabitEthernet0/3",
    "software_version": "7.10 (stable) Jun/15/2023 05:17:29",
    "capabilities": "Router"}

    # insert cdp neighbours parameters into cdpneighbor table
    insert_cdpneihbor([
            (
        	device["hostname"],
            device["destination_host"],
            device["management_ip"],
            device["platform"],
            device["remote_port"],
            device["local_port"],
            device["software_version"],
            device["capabilities"],
            ),
    ])