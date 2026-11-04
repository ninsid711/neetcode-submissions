# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        # head -> 1 -> 2 -> 3 -> NULL ==> NULL <- 1 <- 2 <- 3 <- head
        while curr:
            nxt = curr.next # Save curr.next link's address
            curr.next = prev # Point to previous node (Will point to NULL for starting node)  
            prev = curr # Move prev to point to current node
            curr = nxt # Move curr to next node's location using previously saved link's address
        return prev # Return prev since it points to the new head (curr points to NULL now)