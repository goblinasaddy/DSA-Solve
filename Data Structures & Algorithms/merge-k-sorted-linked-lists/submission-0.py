# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if (lists == []) or (lists == [[]]):
            return None

        nodes = []
        
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                nodes.append(curr.val)
                curr = curr.next

        nodes.sort()
        dummy = ListNode()
        curr = dummy

        for num in nodes:
            node = ListNode(num)
            curr.next = node
            curr = curr.next

        return dummy.next

        