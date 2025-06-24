import sqlite3 # this is part of the Python standard library

def createDB():
    '''Create a database and a table within it'''
    # we need a DB connection object
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # we write an SQL statement
    st = 'CREATE TABLE IF NOT EXISTS zoo (creature VARCHAR(32) PRIMARY KEY, count int, cost float)'
    
    try:
        # next we execute this statement on our database
        curs.execute(st) # no changes happen to the DB
        conn.commit()    # any changes will happen here
        conn.close() # always a good idea to release resources we no longer need
    except Exception as err:
        print(err)


if __name__ == '__main__':
    createDB()