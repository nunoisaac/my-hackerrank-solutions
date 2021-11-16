# Count the number of possible Binary Search Trees with n nodes.
# Examples:
# 1. Input: 1; Output: 1; (Only one tree is possible with 1 node)
# Test Case #2: Two trees can be created using two nodes.
# 1          2
#  \        /
#   2      1

# Test Case #3:

# 1          1         2         3        3
#  \          \       / \       /        /
#   2          3     1   3     1        2
#    \        /                 \      /
#     3      2                   2    1


# Recursive solution
def count_binary_search_tree(n):
    if n == 0:
        return 1

    def helper(root, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        return count_binary_search_tree(root - 1) * count_binary_search_tree(n - root)

    total = 0
    for i in range(1, n + 1):
        total += helper(i, n)
    return total


# memoized solutions
def count_binary_search_tree_2(n):
    def help_count_trees(n, cache):
        if n in cache:
            return cache[n]

        def helper(root, n, cache):
            return help_count_trees(root - 1, cache) * help_count_trees(n - root, cache)

        total = 0
        for i in range(1, n + 1):
            total += helper(i, n, cache)
        cache[n] = total
        return cache[n]

    cache = {0: 1}
    return help_count_trees(n, cache)


# Iterative solution
def count_binary_search_tree_3(n):
    if n == 0 or n == 1:
        return 1
    cache = {0: 1, 1: 1}
    total = 0
    for tree in range(2, n + 1):
        for root in range(1, tree + 1):
            total += cache[root - 1] * cache[tree - root]
        cache[tree] = total
        total = 0
    return cache[n]


# n = 100  # 896519947090131496687170070074100632420837521538745909320
n = 1000   # 204610552146802169264....18184109046864244732001962029120
print(count_binary_search_tree_3(n))
