import math
def solution(X, Y, D):
    # write your code in Python 3.6
    n = math.ceil((Y-X)/D)
    if (n < 0):
        return 0
    else:
        return n