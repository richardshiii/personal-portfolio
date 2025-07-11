'''
21. Merge Two Sorted Lists
Difficulty: Ease
https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing 
together the nodes of the first two lists.
Return the head of the merged linked list.

Example
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
# Solution
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1):
        #建一个新的链表 curr指向头节点方便后续操作
        new_head = ListNode()
        curr = new_head
        #遍历直到链表末尾
        while list1 and list2:
            #比较两个链表同一个位置节点的值 更小值的节点作为输出链表的下一个节点
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            #指向下一个节点
            curr = curr.next
        #如果两个链表长度不一样
        #因为输入的是排序链表 如果任意链表有剩余元素必然比之前的值要大 
        #所以直接连接在输出链表后面即可
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        #new_head只是指向输出链表的头节点,所以return new_head.next
        return new_head.next
    
'''
Test Case
list1 = [1,2,4]
list2 = [1,3,4]
Output
[1,1,2,3,4,4]
'''