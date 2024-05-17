from listNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry
            carry = val // 10
            val %= 10
            cur.nxt = ListNode(val)

            cur = cur.nxt
            l1 = l1.nxt if l1 else None
            l2 = l2.nxt if l2 else None
        return dummy.nxt