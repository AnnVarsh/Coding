class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
        if len(strs)<1:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while(strs[i].find(prefix)!= 0):
                prefix = prefix[:-1]
                if len(prefix)==0:
                    return ""
                    
        return prefix