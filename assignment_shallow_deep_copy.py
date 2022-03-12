import copy

# here we are assigning a value to b, means we are providing a's memory location to b, 
# so when we change any element in b, the a values also change 
# because both are pointing to same memory locatim

def assignmentExample():
    a = [2,3,4]
    b = a
    b[0] = 2
    print(b, a)


# shallow copy is one level deep copy
def shallowCopy():
    a = [2,3,4]
    b = copy.copy(a)
    c = [[1,2],[4,5]]
    d = copy.copy()
    print(a,b)
    print(c,d)

def deepCopy():
    a = [[1,2],[3,4]]
    b = copy.deepcopy(a)
    print(a,b)