def xplus(X, F):
    X_plus = X
    while True:
        oldX_plus = X_plus
        for Y, Z in F:
            if Y <= X_plus:
                X_plus = X_plus | Z
        if oldX_plus == X_plus:
            break
    return X_plus

# Schema
S = {'ssn', 'ename', 'pnumber', 'pname', 'plocation', 'hours'}
# 3 Functional dependencies: 1st part functionally determines the 2nd part

F = [({'ssn'}, {'ename'}),
({'pnumber'}, {'plocation', 'pname'}),
({'pnumber', 'ssn'}, {'hours'})]
print(xplus({'ssn'}, F))
print(xplus({'pnumber'}, F))
print(xplus({'ssn', 'pnumber'}, F))

###########################################################

def xplus(X, F):
    X_plus = X
    while True:
        oldX_plus = X_plus
        for Y, Z in F:
            if Y <= X_plus:
                X_plus = X_plus | Z
        if oldX_plus == X_plus:
            break
    return X_plus

def is_superkey(K, S, F):
    if xplus(K, F) == S:
        return True;
    else:
        return False

# Schema
S = {'ssn', 'ename', 'pnumber', 'pname', 'plocation', 'hours'}
# 3 Functional dependencies: 1st part functionally determines the 2nd part

F = [({'ssn'}, {'ename'}),
({'pnumber'}, {'plocation', 'pname'}),
({'pnumber', 'ssn'}, {'hours'})]
print(is_superkey({'ssn', 'pnumber'}, S, F))
print(is_superkey({'ssn'}, S, F))
print(is_superkey({'ssn', 'pnumber','ename'}, S, F))

#####################################################

def xplus(X, F):
    X_plus = X
    while True:
        oldX_plus = X_plus
        for Y, Z in F:
            if Y <= X_plus:
                X_plus = X_plus | Z
        if oldX_plus == X_plus:
            break
    return X_plus

def covers(F, G):
    for X, Y in G:
        if Y.issubset(xplus(X, F)) != True:
            return False
    return True

def equiv(F, G):
    if covers(F, G) == True and covers(G, F) == True:
        return True;
    else:
        return False

S = {'a', 'c', 'd', 'e', 'h'}
F = [({'a'}, {'c'}),
({'e'}, {'a','h'})
]
G = [({'a'}, {'c'}),
({'a','c'}, {'d'}),
({'e'}, {'a','d'}),
({'e'}, {'h'})
]
print(covers(F, G))
print(covers(G, F))
print(equiv(F, G))