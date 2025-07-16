'''
23. Merge k Sorted Lists
Difficulty: Hard
https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
'''
# Solution
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeKLists(self, lists):
        # T: O(n log k): where N is the total number of nodes across all lists, 
        # and k is the number of input lists.
        # S: O(1): merge in-place, excluding recursive call stack & the result list
        # edge cases
        if not lists or len(lists) == 0:
            return None
        # take pairs of linked list and merge them each time until only one linked list left
        while len(lists) > 1:
            mergedLists = []
            # traverse the list of lists in pairs (i and i+1)
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # check if there is a second list to merge with
                # if not, just merge with None
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            # update the list of lists with the merged results
            lists = mergedLists
        # finally there is only one list left, which is the fully merged sorted list
        return lists[0]
    
    # helper function to merge two sorted linked lists    
    def mergeList(self, l1, l2):
        tail = dummy = ListNode()
        # traverse both lists and add the smaller node to the merged list
        while l1 and l2:
            if l2.val < l1.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next 
        # Append any remaining nodes (only one of l1 or l2 may have nodes left)
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next
    
'''
Test Case
lists = [[1,4,5],[1,3,4],[2,6]]
Output
[1,1,2,3,4,4,5,6]
'''