import sqlite3

def updateDB(w):
    '''implement changes to one row in the DB'''
    count = int(float(w['count']))
    creature = w['creature']
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = f'''
    UPDATE zoo
    SET count={count}
    WHERE creature LIKE "%{creature}%"
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    which = input('Which creature: ')
    w = {'creature':which, 'count':129}
    updateDB(w)