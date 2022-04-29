# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        median_index = (len(nums1) + len(nums2)) // 2
        is_middle = False if (len(nums1) + len(nums2)) % 2 else True
        if is_middle:
            median_index -= 1
        i = 0
        j = 0
        if len(nums1) == 0:
            res = nums2[0]
        elif len(nums2) == 0:
            res = nums1[0]
        else:
            res = min(nums1[0], nums2[0])
        cur = -1

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res = nums1[i]
                i += 1
            else:
                res = nums2[j]
                j += 1
            cur += 1
            if cur == median_index:
                break
        while i >= len(nums1) and cur != median_index:
            res = nums2[j]
            j += 1
            cur += 1
        while j >= len(nums2) and cur != median_index:
            res = nums1[i]
            i += 1
            cur += 1

        if is_middle:
            if i >= len(nums1):
                next = nums2[j]
            if j >= len(nums2):
                next = nums1[i]
            if i < len(nums1) and j < len(nums2):
                next = min(nums1[i], nums2[j])
            res = (next + res) / 2
        return res
