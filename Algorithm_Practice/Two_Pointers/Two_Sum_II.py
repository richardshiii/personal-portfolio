'''
167. Two Sum II - Input Array is Sorted
Difficulty: Medium
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers 
such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''
# Solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # T: O(n) since each pointer iterates at most once through the array
        # S: O(1) no extra space is needed
        # use two pointers, one at the start of the input array, one at the end
        i = 0
        j = len(numbers) - 1
        # use while loop to control the iteration
        # move left pointer to the right, right pointer to the left, until they meet
        # if i+j > target: move j to the left, since nums is in non-decreasing order,
        # we can only get values bigger than the target by moving i to the right
        # if i+j < target: move i to the right
        # if j+j = target: return [i+1, j+1] since the array is 1-indexed
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else: 
                return [i+1, j+1]
            
'''
Test Case
numbers = [2,7,11,15]
target = 9
Output
[1,2]
'''