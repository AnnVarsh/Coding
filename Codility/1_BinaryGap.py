def solution(N):
    # write your code in Python 3.6
    return len(max(format(N, 'b').strip('0').split('1')))