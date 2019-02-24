def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    index = 1
    if (len(A) == 0 or A[0]!=1):
        return 1
    if A[len(A)-1] == len(A):
        return len(A)+1
    else:
        while (index < len(A)):
            if (A[index] - A[index-1] !=1):
                return A[index]-1
            else:
                index+=1