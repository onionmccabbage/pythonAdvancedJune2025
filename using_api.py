import requests

apiURL = 'https://jsonplaceholder.typicode.com'

def getAllData():
    '''retrieve all the JSON from an API end-point'''
    global apiURL
    # make a request for 'photos'
    response = requests.get(f'{apiURL}/photos')
    data = response.json() # or text or xml....
    # return response data
    return data


def getOneData(n):
    '''retrieve a specific member from an API end-point'''
    global apiURL
    response = requests(f'{apiURL}/photos/{n}')
    data = response.json()
    return data


if __name__ == '__main__':
    r = getAllData()
    print(r, type(r)) # we have a list of dict
    # for _ in r:
    #     print(_)
    i = getOneData(42)
    print(i, type(i))