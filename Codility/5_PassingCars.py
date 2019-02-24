
def solution(A):
    # write your code in Python 3.6
    passing_pairs = 0
    zeros = 0
    for i in range(len(A)):
        if A[i] == 0:
            zeros = zeros+1
        else:
            passing_pairs = passing_pairs+zeros
        if passing_pairs>1000000000:
            return -1
    return passing_pairs