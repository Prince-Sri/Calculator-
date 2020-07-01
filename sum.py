
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def inp():



    x =int(input('enter First number'))
    y =int(input('enter second number'))

    7


    choice = input ('enter choice')

    if choice == '1' :

        return (add(x,y))

    elif choice == '2':
        return (sub(x,y))

    elif choice == '3' :
        return (mul(x,y))

    elif choice == '4' :
        return (div(x,y))

    elif choice == '0':

        return ('out')

    
print(inp())
