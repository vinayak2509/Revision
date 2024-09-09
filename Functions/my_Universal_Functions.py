def checkIfNotNumeric(*args):
    retValue = True
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True
def addAllNumerics(*args):
    s=0
    for i in args:
        s+=i
    return s
myName= "Python Revision"
