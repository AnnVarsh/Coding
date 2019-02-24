class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 2:
            return 0
        
        prime_count = [True] * n
        prime_count[0] = prime_count[1] = False
        for i in range(2, n):
            if prime_count[i] == True:
                for j in range(2, (n-1)//i+1):
                    prime_count[i*j] = False
        return sum(prime_count)