def sortIntegers(self, A):
    if not A:
        return None
    for i in range(len(A)-1):# n length, n-1 loops each loop, length is n-i
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A