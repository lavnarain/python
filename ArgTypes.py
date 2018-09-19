#Default Parameters:

def squaring(r=5):
    return r**2

def multipli(a=4,b=5):
    return a*b

#--------------------------------------------------
#VAriable Length parameters:

def VarLen(*argv):
    sum=0
    print(argv)
    for x in argv:
        sum = sum+x
    return sum

#---------------------------------------------------
#keyword Parameters:

def keyfunc(**argv):
    print(argv)
    for x in argv:
        print(x)