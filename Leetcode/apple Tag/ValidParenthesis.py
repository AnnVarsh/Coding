class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        dict1 = {"]":"[","}":"{",")":"("}
        
        for bracket in s:
            if bracket in dict1.values():
                
                stack.append(bracket)
            elif bracket in dict1.keys():
                if stack==[] or dict1[bracket] != stack.pop():
                    return False
            else:
                return False
        return stack==[]