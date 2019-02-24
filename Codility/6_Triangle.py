def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    
    for i in range(len(A)-2):
        if ((A[i] + A[i+1]) > A[i+2]):
            return 1
        else:
            continue
    return 0