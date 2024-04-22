class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head = head.next)
            head.next.next = head

        head.next = None
        return newHead
    
