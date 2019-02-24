def solution(A, K):
    # write your code in Python 3.6
    if (len(A) == 0):
        return A
    else:
        K = K % len(A)
        return A[-K:]+A[:-K]