import requests

def getData(*args):
    '''If no positional arguemnts exist, fetch all the data
    If a single integer positional argument has been provided, just fetch that data  '''
    api_URL = 'https://jsonplaceholder.typicode.com'
    if len(args)==0:
        # get all the data
        url_use = f'{api_URL}/photos'
    elif len(args)==1 and type(args[0])==int:
        url_use  =f'{api_URL}/photos/{args[0]}'
    else:
        raise TypeError('Id must be an integer')
    r = requests.get(url_use)
    return r.json()


if __name__ == '__main__':
    all = getData()
    one = getData(3)
    print(all, one)
    getData(False)