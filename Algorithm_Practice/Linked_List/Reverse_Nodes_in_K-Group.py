'''
25. Reverse Nodes in k-Group
Difficulty: Hard
https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150

Given the head of a linked list, reverse the nodes of the list k at a time, 
and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''
# Solution
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # T: O(n): each node is visited only once
        # S: O(1): no extra space needed, reverse done in-place
        dummy = ListNode()
        dummy.next = head
        # make sure there is 1 node before the group that is being reversed
        # point to the node before the group being reversed, starts at dummy node
        groupPrev = dummy
        # find the kth node from groupPrev to determine the group to reverse
        while True:
            kth = self.getKth(groupPrev, k)
            # if the last group has less than k elements:
            # break out of the loop -> left-out node should remain as it is
            if not kth:
                break
            # store the node immediately after the kth node as the start of the next group
            groupNext = kth.next

            # reverse the linked list
            prev, cur = kth.next, groupPrev.next
            while cur != groupNext:
                # temporarily store the current node
                tmp = cur.next
                # reverse current node's pointer
                cur.next = prev
                # move prev forward
                prev = cur
                # move cur forward to continue 
                cur = tmp
            # after reversal:
                # groupPrev.next is the tail of the group
                # prev is the new head of the reversed group
            tmp = groupPrev.next # save teh current head
            groupPrev.next = kth # connect previous part to new group head
            groupPrev = tmp # move groupPrev to the end of reversed group
        
        return dummy.next
    
    # helper function to locate the group
    # return the kth node from teh current node
    # return None if there are fewer than k nodes left
        while cur and k > 0:
            cur = cur.next
            k -=1
        return cur
'''
Test Case
head = [1,2,3,4,5]
k = 2
Output
[2,1,4,3,5]
'''