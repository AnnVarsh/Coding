class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        words_match = []
        for i in words:
            dict1 = {}
            flag = 1
            if len(i)!=len(pattern):
                continue
            for x,y in zip(pattern,i):
                if x not in dict1.keys():
                    if y not in dict1.values():
                        dict1[x] = y
                    else:
                        flag = 0
                        break
                else:
                    if dict1[x]!= y:
                        flag=0
                        break

            if flag==1:
                words_match.append(i)
                
        return words_match