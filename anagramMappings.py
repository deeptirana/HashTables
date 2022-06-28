class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        prob = {}
        res = []
        for i in range(len(nums2)):
            if nums2[i] not in prob:
                prob[nums2[i]] = i
        for j in range(len(nums1)):
            if nums1[j] in prob:
                res.append(prob[nums1[j]]) 
                
        return res
