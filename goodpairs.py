class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        prob = {}
        res = 0
        for i in nums:
            if i in prob:
                res +=prob[i]
                prob[i] +=1
            else:
                prob[i] = 1
                
        return res 
