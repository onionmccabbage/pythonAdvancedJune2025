import sqlite3

def customRead(w):
    '''retrieve only matching database members'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = f'''
    SELECT creature, count, cost
    FROM zoo
    WHERE creature LIKE "%{w}%"
    '''
    try:
        curs.execute(st)
        conn.commit() # not needed here
        rows = curs.fetchall()
        conn.close()
        return rows
    except Exception as err:
        print(err)

if __name__ == '__main__':
    # NB input is ALWAYS a string
    which = input('Which creature: ')
    match = customRead(which)
    for i in match:
        print(f'we have {i[1]} {i[0]} each costing {i[2]}')
