class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        flag = False
        sortednums = sorted(nums)
        if sortednums[len(nums)-1]/2 >= sortednums[len(nums)-2]:
            maxnum = sortednums[len(nums)-1]
            flag = True
        if flag == True:
            for i in range(len(nums)):
                if maxnum == nums[i]:
                    return i
        return -1