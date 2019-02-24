class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # if x%10 == 0:
        #     x = x//10

        if x > 0:
            s = str(x)
            reversedint =  int(s[::-1])
        else:
            s = str(-1*x)
            reversedint = -int(s[::-1])
        
        if (reversedint <= -2**31 or reversedint >= (2**31)-1):
            return 0
        else:
            return reversedint