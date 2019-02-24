def solution(A):
    # write your code in Python 3.6
    # Using Pigeon Hole principle
    
    list1 = [False]*(len(A)+1)
    
    for i in A:
        if i >= 1 and i <= len(A) + 1:
            list1[i-1] = True
    for i in range(len(A)+1):
        if list1[i]==False:
            return i+1