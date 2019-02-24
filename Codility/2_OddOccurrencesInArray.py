def solution(A):
    # write your code in Python 3.6
    dict1 = {}
    for i in A:
        if i in dict1:
            dict1[i]=dict1[i]+1
        else:
            dict1[i]=1
            
    for i in dict1:
        if (dict1[i]%2)==1:
            return i