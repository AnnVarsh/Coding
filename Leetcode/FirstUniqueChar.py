class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        slist = list(s)
        
        letterfreq = collections.Counter(slist)
        for index, value in enumerate(slist):
            if (letterfreq[value]==1):
                return index
        
        return -1