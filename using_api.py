import requests

apiURL = 'https://jsonplaceholder.typicode.com'

def getAllData():
    '''retrieve all the JSON from an API end-point'''
    global apiURL
    # make a request for 'photos'
    try:
        response = requests.get(f'{apiURL}/photos')
        data = response.json() # or text or xml....
        # return response data
        return data
    except Exception as err:
        print(err)


def getOneData(n):
    '''retrieve a specific member from an API end-point'''
    # global apiURL
    # we may refer to this as REST representation of state (transfer)
    try:
        response = requests.get(f'{apiURL}/photos/{n}')
        data = response.json()
        return data
    except Exception as err:
        print(err)

if __name__ == '__main__':
    r = getAllData()
    print(r, type(r)) # we have a list of dict
    # for _ in r:
    #     print(_)
    i = getOneData(42)
    print(i, type(i))