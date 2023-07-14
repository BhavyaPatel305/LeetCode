import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_1 = np.array(nums1)
        nums_2 = np.array(nums2)
        nums_3 = np.concatenate((nums_1, nums_2))
        sorted_array = np.sort(nums_3)
        return np.median(sorted_array)
    
