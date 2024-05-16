from listNode import ListNode

"""Floyd's cycle finding algorithm is used in this."""

class Solution:
    def hasCycle(self, head: ListNode)-> bool:
        slow, fast = head, head

        while fast and fast.nxt:
            slow = slow.nxt
            fast = fast.nxt.nxt
            if slow == fast:
                return True

        return False