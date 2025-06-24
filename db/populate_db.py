import sqlite3

def populateDB(c_t):
    '''iterate over a collection to place new creatures into our DB'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st   = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''

    # the '?' lets us inject values
    for item in c_t:
        # validate the members
        try:
            if type(item['creature'])==str:
                # assign to clean data
                n = item['creature']
            else:
                raise Exception('Creature name must be a string')
            if type(item['count'])==int:
                count = item['count']
            else:
                raise Exception('Count must be an integer')
            if type(item['cost']) in (int, float):
                cost = item['cost']
            else:
                raise Exception('Cost must be in or float')
            curs.execute(st, (n, count, cost))
            conn.commit()
        except Exception as err:
            print(err)
    conn.close() # tidy up!!

if __name__ == '__main__':
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    ) 
    populateDB(creatures_t)