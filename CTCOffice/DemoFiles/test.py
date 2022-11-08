# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode(object):
    pass


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1.val <= list2.val:
            curPtr = list1
            returnPtr = curPtr

            list1 = list1.next
            curPtr.next = list1
            curPtr = list1
        else:
            curPtr = list2
            returnPtr = curPtr

            list2 = list2.next
            curPtr.next = list2
            curPtr = list2

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curPtr.next = list1
                curPtr = list1
                list1 = list1.next
            else:
                curPtr.next = list2
                curPtr = list2
                list2 = list2.next

        if list1 is not None:
            curPtr.next = list1
        elif list2 is not None:
            curPtr.next = list2

        return returnPtr