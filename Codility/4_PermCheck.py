def solution(A):
    # write your code in Python 3.6
    truesum = len(A)*(len(A)+1)/2
    
    if sum(A) == truesum and max(A) == len(set(A)):
        return 1
    else:
        return 0