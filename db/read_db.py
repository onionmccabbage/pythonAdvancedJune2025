import sqlite3

def readDB():
    '''read back all entries from our database'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = '''
    SELECT creature, cost, count FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit() # not actually needed here
        # we may have a result come back from the DB
        rows = curs.fetchall()
        conn.close()
        return rows # this will be a list
    except Exception as err:
        print(err)

if __name__ == '__main__':
    r = readDB()
    print(r, type(r))
    for a in r:
        print(f'We have {a[2]} {a[0]} costing {a[1]}')