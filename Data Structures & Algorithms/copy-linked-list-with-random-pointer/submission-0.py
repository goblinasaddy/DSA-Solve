"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newlist = {None:None}

        curr = head
        while curr:
            newlist[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = newlist[curr]
            copy.next = newlist[curr.next]
            copy.random = newlist[curr.random]
            curr = curr.next

        return newlist[head]