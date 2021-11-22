""""
HackerRank: Recursion: Davis' Staircase

Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or  steps at a time. 
Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
Given the respective heights for each of the  staircases in his house, find and print the number of ways he 
can climb each staircase, module 10^10 + 7 on a new line.

Example
n = 5
The staircase has 5 steps. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2

There are 13 possible ways he can take these 5 steps and 13 modulo 100000000007 = 13

Function Description

Complete the stepPerms function using recursion in the editor below.

stepPerms has the following parameter(s):

int n: the number of stairs in the staircase


Returns

int: the number of ways Davis can climb the staircase, modulo 10000000007


Input Format

The first line contains a single integer, s, the number of staircases in his house.
Each of the following s lines contains a single integer, n, the height of staircase i.

Sample Input

STDIN   Function
-----   --------
3       s = 3 (number of staircases)
1       first staircase n = 1
3       second n = 3
7       third n = 7


1
4
44


My Solution:
"""
def stepPerms(n):
    def tab_step(num_stairs, cache):

        for i in range(1, num_stairs + 1):
            if num_stairs in cache:
                return cache[num_stairs]
            if i >= 2:
                cache[i] = (
                    cache.get(i - 1, 0) + cache.get(i - 2, 0) + cache.get(i - 3, 0)
                )
            else:
                cache[i] = cache.get(i - 1, 0)
        return cache[num_stairs]

    cache = {0: 1, 1: 1}
    return tab_step(n, cache)


"""
Here is a similar problem called ways to step:

A child can climb the stairs by advancing 1 step, 2 steps or 3 steps at a time.  If the child has n steps in 
between base and top, how many different ways can the child go from the base to the top?
Examples:

1. Input: 2; Output: 4; (If there are 2 steps between base and top, the child can reach the top in 4 ways)
2. Input: 3; Output: 7; (If there are 3 steps between base and top, the child can reach the top in 7 ways)
3. Input 4: Ouput: 13
4. Input 0: Output: 1
"""

# Recursive solution
def ways_to_step(num_stairs):

    # -1 since top step counts as a step
    # and num_stairs represent only the steps between base and top
    if num_stairs == 0 or num_stairs == -1:
        return 1

    # num_stairs is 2 + top is 3 steps total
    if num_stairs >= 2:
        return (
            ways_to_step(num_stairs - 1)
            + ways_to_step(num_stairs - 2)
            + ways_to_step(num_stairs - 3)
        )
    if num_stairs == 1:
        return ways_to_step(num_stairs - 1) + ways_to_step(num_stairs - 2)

# Memoized solution
def ways_to_step_memo(num_stairs):
    def helper(num_stairs, cache):

        if num_stairs in cache:
            return cache[num_stairs]

        if num_stairs <= 0:
            cache[num_stairs] = 1
            return cache[num_stairs]

        if num_stairs >= 2:
            cache[num_stairs] = (
                helper(num_stairs - 1, cache)
                + helper(num_stairs - 2, cache)
                + helper(num_stairs - 3, cache)
            )
            return cache[num_stairs]
        else:
            cache[num_stairs] = helper(num_stairs - 1, cache) + helper(
                num_stairs - 2, cache
            )
            return cache[num_stairs]

    cache = {-1: 1, 0: 1}
    return helper(num_stairs, cache)

# Iterative/Tabulated solution
def ways_to_step_tab(num_stairs):
    def tab_step(num_stairs, cache):

        for i in range(1, num_stairs + 1):
            if num_stairs in cache:
                return cache[num_stairs]
            if i >= 2:
                cache[i] = (
                    cache.get(i - 1, 0) + cache.get(i - 2, 0) + cache.get(i - 3, 0)
                )
            else:
                cache[i] = 2*cache.get(i-1, 0)
        return cache[num_stairs]

    cache = {-1: 1, 0: 1}
    return tab_step(num_stairs, cache)


"""
Leetcode:
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45


My solution, similar to the solutions above:
"""
def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    # -1 and 0 are added since n is the number of stairs between base and top step
    cache = {-1:1, 0:1}  

    for i in range(1,n+1):
        if n in cache:
            return cache[n]
        if i >= 2: 
            cache[i] = cache.get(i-1, 0) + cache.get(i-2, 0)
        else: 
            cache[i] = cache.get(i-1, 0)
    return cache[n]