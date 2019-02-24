class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev = []
        for i in s.split(" "):
            rev.append(i[::-1])
        
        return " ".join(rev)