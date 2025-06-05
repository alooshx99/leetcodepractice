class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        fullarr = sorted(nums1 + nums2)
        if len(fullarr)%2 == 0:
            return float( ( fullarr[ len(fullarr)/2 ] + fullarr[ len(fullarr)/2 -1 ]) / 2.00 )
        
        return float( fullarr[ len(fullarr)//2 ] )

        
