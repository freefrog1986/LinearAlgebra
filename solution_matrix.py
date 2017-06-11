
def shape(M):
    r = len(M)
    c = len(M[1])
    return r,c

# TODO in-place operation, no return value
# TODO round all elements in M to decPts
def matxRound(M, decPts=4):
    r,c = shape(M)
    i = 0
    while i<r:
        j = 0
        while j<c:
            M[i][j] = round(M[i][j],decPts)
            j += 1
            pass
        i += 1
        pass
    return M

#TODO compute transpose of M
def transpose(M):
    r,c = shape(M)
    Mt = []
    j = 0
    while j<c:
        temp =[]
        i = 0
        while i<r:
            temp += [M[i][j]] 
            i += 1
        Mt.append(temp)
        j += 1
    return Mt

#TODO compute matrix multiplication AB, return None if the dimensions don't match
def matxMultiply(A, B):
    ar,ac = shape(A)
    br,bc = shape(B)
    C = []
    if not ac == br:
        return None
    else:
        
        return 

# 1.1 Create a 4*4 identity matrix
A = [[1,2,3], [2,3,3], [1,2,5]]
B = [[1,2,3,5], [2,3,3,5], [1,2,5,1]]
I = [[1,0,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]]
# print A,B,I

# 1.2 get the width and height of a matrix
# print shape(A),shape(B),shape(I)

# 1.3 round all elements in M to certain decimal points
# print matxRound(B)

# 1.4 compute transpose of M
# print transpose(B)

# 1.5 compute AB. return None if the dimensions don't match
print matxMultiply(A,I)








