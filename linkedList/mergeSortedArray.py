class ListNode:
    def __init__(self, val: int, nxt=None):
        self.val = val
        self.nxt = nxt


class Solution:
    def mergeTwoSortedArray(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.nxt = list1.val
                list1 = list1.nxt
            else:
                tail.nxt = list2.val
                list2 = list2.nxt

            tail = tail.nxt

        if list1:
            tail.nxt = list1
        elif list2:
            tail.nxt = list2

        return dummy.nxt


ans = Solution()
