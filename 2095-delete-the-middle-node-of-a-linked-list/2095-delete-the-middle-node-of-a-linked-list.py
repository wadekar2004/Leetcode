# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next==None:
            return None
        prev=None
        slow=head
        fast=head

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head
# Use 2 pointers.
# One is
# Slow
# Another
# Fast
# Rule
# Slow
# moves 1 step
# ↓

# Fast

# moves 2 steps

# Suppose

# 1 → 3 → 4 → 7 → 1 → 2 → 6

# Initially

# S
# F

# ↓

# 1 → 3 → 4 → 7 → 1 → 2 → 6
# Move 1

# Slow

# 3

# Fast

# 4
# 1 → 3 → 4 → 7 → 1 → 2 → 6
#     S   F
# Move 2

# Slow

# 4

# Fast

# 1
# 1 → 3 → 4 → 7 → 1 → 2 → 6
#         S       F
# Move 3

# Slow

# 7

# Fast

# 6
# 1 → 3 → 4 → 7 → 1 → 2 → 6
#             S           F
        