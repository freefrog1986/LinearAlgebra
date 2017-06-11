
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

def listMultiply(A,B):
    t = 0
    l1=len(A)
    i = 0
    while i<l1:
        t+=A[i]*B[i]
        i+=1
    return t

#TODO compute matrix multiplication AB, return None if the dimensions don't match
def matxMultiply(A, B):
    ar,ac = shape(A)
    br,bc = shape(B)
    if not ac == br:
        return None
    else:
        C = []
        Bt = transpose(B)
        for i in A:
            t = []
            for j in Bt:
                t += [listMultiply(i,j)]
            C.append(t)
        return C

# 1.1 Create a 4*4 identity matrix
A = [[1,2,3], [2,3,3], [1,2,5]]
B = [[1,2,3,5], [2,3,3,5], [1,2,5,1]]
I = [[1,0,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]]
# print A,B,I

# Test your implementation

#TODO test the shape function
print shape(A),shape(B),shape(I)

#TODO test the round function
print matxRound(B)

#TODO test the transpose funtion
print transpose(B)

#TODO test the matxMultiply function, when the dimensions don't match
print matxMultiply(A,I)

#TODO test the matxMultiply function, when the dimensions do match
print matxMultiply(A,B)






