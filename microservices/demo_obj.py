import flask_server

def fn():
    def fnX(): # everything is just an object
        return 'inside'
    r = fnX()
    return r

# watch out - you can use ANYTHING as the key in a dict
d = {'n':'Ethel', True:'wow', fn:None}

l = [fn, d, flask_server]

print( fn() )