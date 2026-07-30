# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        left=head
        right=prev

        max_sum=0

        while right:
            current_sum=left.val+right.val

            if current_sum > max_sum:
                max_sum=current_sum
            left=left.next
            right=right.next
        return max_sum
        