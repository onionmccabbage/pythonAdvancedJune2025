# Python has tools to work with JSON data
import json

def useJSON(struct):
    '''convert between Python data structure and JSON'''
    j = json.dumps(struct) # 'dumps' will convert any Python structure to a JSON text 
    return j # return the JSON text

def makeStruct(text):
    '''convert some JSON text into a structure'''
    s = json.loads(text)
    return s

def readJSON(fn):
    '''Read in JSON text from a specified file name'''
    try:
        fin = open(fn, 'rt') # we now have a file access object
        f = json.load(fin) # NB the file must contain valid JSON
        return f # the text will automatically be converted to a Python dict or list
    except Exception as err:
        print(err)

if __name__ == '__main__':
    # try to load JSON from an external file
    result = readJSON('photos.json')
    print(result, type(result))


    my_data = {'main':'eggs', 'side':'salad', 'after':'icecream'}
    print(my_data, type(my_data)) # a dict
    my_data_j = useJSON(my_data)
    print(my_data_j, type(my_data_j))
    # this works for all Python structures
    my_list = ['apple', 'orange', 'durian']
    my_list_j = useJSON(my_list)
    print(my_list_j, type(my_list_j)) # a string

    # we can go from text to JSON
    t = '''{"id":1, "name":"Oenid", "level":"admin"}'''
    s = makeStruct(t)
    print(s, type(s))
    l = makeStruct(my_list_j)
    print(l, type(l)) # we have a list
