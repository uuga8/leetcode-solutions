class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        nums1_index = m -1
        nums2_index = n -1
        
        for item in range(m+n-1, -1, -1):
            if nums2_index < 0:
                break
            elif nums1_index < 0 or nums1[nums1_index] < nums2[nums2_index]:
                    nums1[item] = nums2[nums2_index]
                    nums2_index -= 1            
            else:
                nums1[item] = nums1[nums1_index]
                nums1[nums1_index] = 0
                nums1_index -= 1

                
                
            
