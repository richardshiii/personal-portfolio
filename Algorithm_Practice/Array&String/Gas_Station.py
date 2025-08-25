'''
134. Gas Station
Difficulty: Medium
https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. 
If there exists a solution, it is guaranteed to be unique.

Example:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
'''
# Solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # T: O(n): iterate through the input arrays once
        # S: O(1): no extra space is required
        # If total gas amount is less than the total cost, the circle can't be completed
        if sum(gas) < sum(cost):
            return -1
        # Initialize the starting point and total gas in the tank
        start_point, total = 0, 0
        # iterate through the input array & calculate the total gas in tank
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            # if total gas in tank is less than 0, 
            # can't travel to the next station from the current starting point
            # so we reset the total gas to 0 
            # move to the next station as starting point & try again
            if total < 0:
                total = 0
                start_point = i + 1
        # return the starting point if loop completes
        return start_point

'''
Test Case
gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output 
3
'''