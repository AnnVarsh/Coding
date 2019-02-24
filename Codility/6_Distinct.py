def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    count = 1
    if len(A) == 0:
        return 0
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            continue
        else:
            count+=1
    return count