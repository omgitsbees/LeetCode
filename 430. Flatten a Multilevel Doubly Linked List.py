"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        # Use a stack to keep track of nodes that have next pointers we need to return to
        stack = []
        curr = head
        
        while curr:
            if curr.child:
                # If current node has a next node, save it for later
                if curr.next:
                    stack.append(curr.next)
                
                # Connect current node to its child
                curr.next = curr.child
                curr.child.prev = curr
                
                # Clear the child pointer
                curr.child = None
            
            # If we reach the end of current branch and have saved nodes
            if not curr.next and stack:
                # Get the next node we saved earlier
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr
            
            curr = curr.next
        
        return head
