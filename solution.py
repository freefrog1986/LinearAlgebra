
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

#TODO construct the augment matrix of matrix A and column vector b, assuming A and b have same number of rows
def augmentMatrix(A, b):
    ar,ac = shape(A)
    i = 0
    while i<ar :
        A[i] += [b[i]]
        i += 1
    return A


# TODO r1 <---> r2
# TODO in-place operation, no return value
def swapRows(M, r1, r2):
    temp = []
    temp = M[r1]
    M[r1] = M[r2]
    M[r2] = temp
    pass

# TODO r1 <--- r1 * scale
# TODO in-place operation, no return value
def scaleRow(M, r, scale):
    t=[]
    for e in M[r]:
        e = e*scale
        t+=[e]
    M[r] = t
    pass

# TODO r1 <--- r1 + r2*scale
# TODO in-place operation, no return value
def addScaledRow(M, r1, r2, scale):
    t=[]
    for e in M[r2]:
        e = e*scale
        t+=[e]
    M[r1]=listAdd(t,M[r1])
    pass

def listAdd(l1,l2):
    len1 = len(l1)
    i = 0
    newlist = []
    while i<len1:
        temp = l1[i] + l2[i]
        newlist+=[temp]
        i+=1
    return newlist

def is_nonzero_row(R,j,epsilon = 1.0e-16):
    if R[j]>epsilon:
        if j>0:
            if max(R[0:j])<epsilon:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def swap_with_nonzero_row_below(M,i,j,epsilon=1.0e-16):
    mr,mc = shape(M)
    num_row = mr-1
    if i < num_row:
        for index_r in range(i+1,mr):
            if is_nonzero_row(M[index_r],j,epsilon):
                swapRows(M,i,index_r)
                return True
            else:
                pass
    else:
        return False
    return False

def first_nonzero_num(l,epsilon=1.0e-16):
    for i in l:
        if i>epsilon:
            return 1./i
        else:
            continue
    return False

# Transform Matrix to reduced row echelon form
def rre_form(M,epsilon=1.0e-16):
    M_copy = M[:]

    mr,mc = shape(M)

    for i in range(mr):
        j=0
        while j<mc:
            # print i,j
            if M_copy[i][j]<epsilon:
                swap_succeeded = swap_with_nonzero_row_below(M_copy,i,j,epsilon)
                if swap_succeeded:
                    j+=1
                    break
            j+=1

    for i in range(mr):
        n = first_nonzero_num(M_copy[i])
        scaleRow(M_copy,i,n)

    return M_copy


#TODO implement gaussian jordan method to solve Ax = b

""" Gauss-jordan method to solve x such that Ax = b.
        A: square matrix, list of lists
        b: column vector, list of lists
        decPts: degree of rounding, default value 4
        epsilon: threshold for zero, default value 1.0e-16
        
    return x such that Ax = b, list of lists 
    return None if A and b have same height
    return None if A is (almost) singular
"""

def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    ar,ac = shape(A)
    br = len(b)
    # print ar,ac
    # print br
    # if not ar == br:



    return None

# 1.1 Create a 4*4 identity matrix
A = [[1,2,3], [2,3,3], [1,2,5]]
B = [[1,2,3,5], [2,3,3,5], [1,2,5,1]]
I = [[1,0,0,0], [0,1,0,0], [0,0,1,0],[0,0,0,1]]
# print A,B,I

# # Test your implementation

# #TODO test the shape function
# print shape(A),shape(B),shape(I)

# #TODO test the round function
# print matxRound(B)

# #TODO test the transpose funtion
# print transpose(B)

# #TODO test the matxMultiply function, when the dimensions don't match
# print matxMultiply(A,I)

# #TODO test the matxMultiply function, when the dimensions do match
# print matxMultiply(A,B)


# b = [9,9,9]
# print A
# print augmentMatrix(A, b)
# print A
# scaleRow(A,1,4)
# print A

# print A
# addScaledRow(A, 1, 2, 2)

# t = [[0,2,2,3,4,5],[0,0,4,1,4,2],[3,1,0,0,2,1],[0,7,2,2,1,1]]
# print t
# print rre_form(t)

# print swap_with_nonzero_row_below(A,0,1)
# t=[0,0,1,1,1]
# print is_nonzero_row(t,2,epsilon = 1.0e-16)

# t = [[0,1,1,1],[1,1,1,1]]
# print t
# print swap_with_nonzero_row_below(t,0,0)
# print t

A = [[0,2,2,3,4,5],[0,0,4,1,4,2],[3,1,0,0,2,1],[0,7,2,2,1,1]]
b = [3,2,1,4]
gj_Solve(A, b)



