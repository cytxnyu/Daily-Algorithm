class ListNode:
    def __init__ (self, val = 0 , next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next 

s = Solution()
L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(3)
L1.next.next.next = ListNode(4)
L1.next.next.next.next = ListNode(5)
result = s.removeNthFromEnd(L1, 2)
while result:
    print(result.val)
    result = result.next
