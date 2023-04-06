def prime(x):
    for i in range (2,x):
        if x%i == 0:
            return False
        else:
            return True
def perfect(x):
    s=0
    for i in range(1,x):
        if x%i == 0:
            s += 1
    return s==x
