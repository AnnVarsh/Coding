def solution(A):
    # write your code in Python 3.6
    first_part = A[0]
    second_part = sum(A[1:])
    min_diff = abs(first_part - second_part)
    
    for p in range(1,len(A)-1):
        first_part = first_part+A[p]
        second_part = second_part-A[p]
        if (abs(first_part - second_part) < min_diff):
            min_diff = abs(first_part - second_part)
    return min_diff