"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        if not head:
        	return None 
        slow = fast = ListNode(0)
        slow.next = head
        while fast:
        	if not fast.next:
        		break
        	slow = slow.next
        	fast = fast.next.next
        return slow 
