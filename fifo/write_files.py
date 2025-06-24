
def writeText(t):
    '''commit text to a file'''
    try:
        # using 'with' will close the file access object when done
        with open('my_file.txt', 'at') as fout:
            fout.write(t)
            # we may choose to add a new line character
            fout.write('\n')
    except Exception as err:
        print(err)


def writeBytes(v):
    '''commit bytes to a file'''
    b = bytes(v, 'UTF8') # b = b'{v}'
    try:
        # 'ab' will append bytes
        with open('my_bytes', 'ab') as foutb:
            foutb.write(b) # commit the bytes to a file
    except Exception as err:
        print(err)    

def seekContent():
    ''''''

if __name__ == '__main__':
    words = 'this is plain text in a file'
    writeText(words)
    writeBytes(words)