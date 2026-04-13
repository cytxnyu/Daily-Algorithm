class ListNode:
    def __init__(self, val= 0 , next = None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1 : ListNode , head2: ListNode ) -> ListNode:
            dummyHead = ListNode(0)
            temp , temp1 , temp2 = dummyHead ,  head1 , head2
            while temp1 and temp2:
                if temp1.val <= temp2.val :
                    temp.next  = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                    