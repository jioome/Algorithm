class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        answer = nums1& nums2
        print(answer)
        answer = list(answer)
        return answer