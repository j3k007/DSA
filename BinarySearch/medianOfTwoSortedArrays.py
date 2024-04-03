class Solution:
    def findMedianSortedArrays(self, nums1:list[int], nums2:list[int]):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums2) > len(nums1):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

ans = Solution()
nums1 = [1,2,3,4,5]
nums2 = [1,2,3,4,5,6,7,8]
print(ans.findMedianSortedArrays(nums1, nums2))