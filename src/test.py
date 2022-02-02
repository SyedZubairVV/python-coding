def myfunctionReturns(name):
    return str(name).upper()


def myfunction(name):
    print(name)


def simpleArraySum(a, b):
    c = 0
    d = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            c = c+1
        elif b[i] > a[i]:
            d = d+1

    return [c, d]


def stairCase(n):
    c = n
    d = c

    for i in range(0, n):
        stri = ""
        c = c - 1
        d = n - c
        for x in range(0, c):
            stri = stri + " "
        for y in range(0, d):
            stri = stri + "#"
        print(stri)
