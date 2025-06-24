
def writeText(t):
    '''commit text to a file'''
    try:
        # using 'with' will close the file access object when done
        # 'xt' will only work with exclusive file access
        with open('my_file.txt', 'xt') as fout: # 'a' will append, 'w' will (over)write
            fout.write(t)
            # we may choose to add a new line character
            fout.write('\n')
    except FileExistsError as fee:
        print(f'File Exisits - try using append or overwrite {fee}')
    #we always end up with a general exception handler
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

if __name__ == '__main__':
    words = 'this is plain text in a file'
    writeText(words)
    writeBytes(words)