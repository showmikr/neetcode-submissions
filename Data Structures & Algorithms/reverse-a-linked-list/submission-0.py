# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head, real_tail = Solution.revList(head)
        return real_tail
    def revList(head: Optional[ListNode]) -> (Optional[ListNode],Optional[ListNode]):
        tail = None
        real_tail = None
        if head and head.next != None:
            r = Solution.revList(head.next)
            tail, real_tail = r[0], r[1]
        else:
            real_tail = head
            return (head, head)
        tail.next = head
        head.next = None
        return (head, real_tail)