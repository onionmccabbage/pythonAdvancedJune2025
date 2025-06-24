# we may choose to pass in as few or as many positional arguments as we like

# other languages allow overloading but not in Python

# by convention we gather all the positional arguments into a tuple called 'args'
def handleResults( *args ): # the asterisk indicates gather the positional arguments
    '''If there are no arguments passed in, we respond that there are no results'''
    # print(args)
    if len(args)==0:
        return f'No positional arguemnts were supplied {args}'
    elif len(args)==1:
        return f'Exactly one positional argument was provided: {args[0]}'
    else:
        return f'More than one positional argument was provided: {args}'

def handleKW(**kwargs): # the double-asterisk indicates gather all the keyword arguments into a dict
    '''respond differently depending on the keyword arguments passed in
    If num_sides and colour and id all exist, return them
    If one or more member is missing, provide a default then return'''
    # print(kwargs, type(kwargs))
    try:
        if kwargs['num_sides']:
            n = kwargs['num_sides']
        # else:
        #     n=4 # a sensible default in case the value is missing
    except KeyError as ke:
        n=4
    try:
        if kwargs['colour']:
            c = kwargs['colour']
    except KeyError as ke:
        c='grey'
    try:
        if kwargs['id']:
            i = kwargs['id']
    except KeyError as ke:
        i=0
    return {'num_sides':n, 'colour':c, 'id':i}

# NB if we pass both args and kwargs they must be args followed by kwargs

if __name__ == '__main__':
    # call our function with no positional arguments, then with one, two...
    r = handleResults()
    print(r)
    r = handleResults(4) 
    print(r)
    r = handleResults(6,3) # positional arguments always appear in order like this
    print(r)
    r = handleResults(7,5,0)
    print(r)
    # exercise our KW function
    s = handleKW()
    print(s)
    s = handleKW(num_sides=7)
    print(s)
    s = handleKW(num_sides=7, colour='blue')
    print(s)
    s = handleKW(num_sides=3, colour='green', id=42)
    print(s)
    