def readText():
    '''retrieve from a text file'''
    try:
        with open('my_file.txt', 'rt') as fin:
            t = fin.read()
        return t        
    except Exception as err:
        print(err)

def readBytes():
    '''retrieve from a byte file'''
    try:
        with open('my_bytes', 'rb') as finb:
            t = finb.read()
            return t
    except Exception as err:
        print(err)     

if __name__ == '__main__':
    print(  readText()  )
    b = readBytes()
    print(b) # this is a byte string