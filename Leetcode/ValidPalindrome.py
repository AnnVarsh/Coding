class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alphanumlist = [c for c in s.lower() if c.isalnum()]
        
        if alphanumlist == alphanumlist[::-1]:
            return True
        else: 
            return False
        