#dynamic programming
# class Solution:
#     def canCross(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: bool
#         """
#         if stones[1] != 1:
#             return False
        
#         d = {x: set() for x in stones}
        
#         d[1].add(1)
        
#         for x in stones[:-1]:
#             for j in d[x]:
#                 for k in range(j-1, j+2):
#                     if k > 0 and x+k in d:
#                         d[x+k].add(k)
                        
#         return bool(d[stones[-1]])


class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        fail=set()
        stoneset=set(stones)
        
        stack=[(0,0)]
        
        while stack:
            stone,jump=stack.pop()
            for j in (jump-1,jump,jump+1):
                s=stone+j
                
                if j>0 and s in stoneset and (s,j) not in fail:
                    if s==stones[-1]:
                        return True
                    stack.append((s,j))
            fail.add((stone,jump))
        return False