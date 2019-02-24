class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return collections.Counter(s) == collections.Counter(t)
        
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in letters:
            if s.count(i) != t.count(i):
                return False
        return True
                    