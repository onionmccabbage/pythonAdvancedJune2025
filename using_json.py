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

if __name__ == '__main__':
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
