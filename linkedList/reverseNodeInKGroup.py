from listNode import ListNode

"""
k is +vs int and k <= len(head)
"""
class Solution:
    def reverseKGroup(self, head: ListNode, k: int)-> ListNode:
        dummy = ListNode(0,None)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNxt = kth.nxt
            prev, curr = kth.nxt, groupPrev.nxt
            while curr != groupNxt:
                tmp = curr.nxt
                curr.nxt = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.nxt
            groupPrev.nxt = kth
            groupPrev = tmp
        return dummy.nxt
        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.nxt
            k -= 1
        return curr