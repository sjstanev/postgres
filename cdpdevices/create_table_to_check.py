from config import config
import psycopg2


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE to_check(
            to_check_id SERIAL PRIMARY KEY,
            hostname VARCHAR(255) NOT NULL,
            management_ip VARCHAR(255) NOT NULL,
            flag VARCHAR(255)
        )
        """,
    )


    conn = None
    try:
        # read the connection parameters
        params = config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # create table one by one
        for command in commands:
            cur.execute(command)

        # close communication with the postgreSQL database server
        cur.close()

        # commit the changes
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()