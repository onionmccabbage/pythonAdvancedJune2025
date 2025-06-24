import sqlite3

def writeDB():
    '''write a record into the dB table'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.52)
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)


if __name__ == '__main__':
    writeDB()