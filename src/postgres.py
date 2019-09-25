"""Helper module for interacting with PostgreSQL"""

import psycopg2 as pg2

def connect_to_postgres():
    """Preconfigured to create a connection to postgres database. 
    
    Returns
    -------
    con, cur : connect_to_postgres()
    """
    
    con = pg2.connect(host='this_postgres', user='postgres', database='postgres')
    
    return con, con.cursor()