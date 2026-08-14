# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collection import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return[]
        queue=deque([root])
        answer=[]

        while queue:
            level_size=len(queue)

            for i in range(level_size):
                node=queue.popleft()
                if i==level_size-1:
                    answer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return answer




#         Absolutely bro. Let's make it **super simple, like explaining to a kid**. No complicated words.

# We'll use this tree:

# ```text
#         1
#        / \
#       2   3
#        \   \
#         5   4
# ```

# Expected answer:

# ```text
# [1, 3, 4]
# ```

# ## Code

# ```python
# from collections import deque

# class Solution:
#     def rightSideView(self, root):

#         if root is None:
#             return []

#         queue = deque([root])
#         answer = []

#         while queue:

#             level_size = len(queue)

#             for i in range(level_size):

#                 node = queue.popleft()

#                 if i == level_size - 1:
#                     answer.append(node.val)

#                 if node.left:
#                     queue.append(node.left)

#                 if node.right:
#                     queue.append(node.right)

#         return answer
# ```

# Now **line by line** 👇

# ---

# ### Line 1

# ```python
# from collections import deque
# ```

# We need a **queue**.

# Think of a queue like children standing in a line:

# ```text
# First child → Second child → Third child
# ```

# The first child who came in goes out first.

# ---

# ### Line 2

# ```python
# class Solution:
# ```

# This is just LeetCode's required class.

# Don't worry about it.

# ---

# ### Line 3

# ```python
# def rightSideView(self, root):
# ```

# Our function receives the tree.

# `root` means the first node:

# ```text
# 1
# ```

# ---

# ### Line 4-5

# ```python
# if root is None:
#     return []
# ```

# If there is no tree:

# ```text
# nothing
# ```

# So return:

# ```text
# []
# ```

# ---

# ### Line 6

# ```python
# queue = deque([root])
# ```

# Put the first node into our queue.

# Our tree starts with `1`.

# So:

# ```text
# queue = [1]
# ```

# Think:

# > "Okay, I will start checking from node 1."

# ---

# ### Line 7

# ```python
# answer = []
# ```

# We need somewhere to store the nodes we can see from the right.

# Currently:

# ```text
# answer = []
# ```

# ---

# # Now the important part

# ### Line 8

# ```python
# while queue:
# ```

# Meaning:

# > "While there are still nodes waiting in the queue, keep working."

# Currently:

# ```text
# queue = [1]
# ```

# So yes, continue.

# ---

# ### Line 9

# ```python
# level_size = len(queue)
# ```

# Ask:

# > "How many nodes are in this level?"

# Currently:

# ```text
# queue = [1]
# ```

# So:

# ```text
# level_size = 1
# ```

# That means this level has **1 node**.

# ---

# ### Line 10

# ```python
# for i in range(level_size):
# ```

# Since:

# ```text
# level_size = 1
# ```

# this runs once:

# ```text
# i = 0
# ```

# We are going to check the one node in this level.

# ---

# ### Line 11

# ```python
# node = queue.popleft()
# ```

# Take the first node out of the queue.

# Before:

# ```text
# queue = [1]
# ```

# Take `1`.

# After:

# ```text
# queue = []
# node = 1
# ```

# ---

# ### Line 12 ⭐

# ```python
# if i == level_size - 1:
# ```

# This is asking:

# > **"Is this the last node of this level?"**

# We have:

# ```text
# i = 0
# level_size = 1
# ```

# So:

# ```text
# level_size - 1
# = 1 - 1
# = 0
# ```

# Therefore:

# ```text
# i == 0
# ```

# YES! `1` is the last node of this level.

# ---

# ### Line 13

# ```python
# answer.append(node.val)
# ```

# Since `1` is the last node of this level, we can see it from the right.

# Put `1` into answer:

# ```text
# answer = [1]
# ```

# ---

# ### Lines 14-15

# ```python
# if node.left:
#     queue.append(node.left)
# ```

# Node `1` has a left child:

# ```text
# 2
# ```

# Put `2` into the queue:

# ```text
# queue = [2]
# ```

# ---

# ### Lines 16-17

# ```python
# if node.right:
#     queue.append(node.right)
# ```

# Node `1` also has right child:

# ```text
# 3
# ```

# Put `3` into queue:

# ```text
# queue = [2, 3]
# ```

# ---

# # Next level

# Now queue is:

# ```text
# [2, 3]
# ```

# These are the nodes on the **second level**.

# ---

# ### Again:

# ```python
# level_size = len(queue)
# ```

# There are 2 nodes:

# ```text
# level_size = 2
# ```

# So we need to process:

# ```text
# 2
# 3
# ```

# ---

# ### First node

# ```python
# node = queue.popleft()
# ```

# Take `2`.

# ```text
# queue = [3]
# node = 2
# ```

# `i = 0`.

# Check:

# ```python
# if i == level_size - 1:
# ```

# ```text
# 0 == 2 - 1
# 0 == 1
# ```

# ❌ No.

# So don't add `2`.

# Why?

# Because `2` is **not the last node of this level**.

# ---

# ### Next node

# Take `3`:

# ```text
# node = 3
# ```

# Now:

# ```text
# i = 1
# ```

# Check:

# ```text
# 1 == 2 - 1
# 1 == 1
# ```

# ✅ YES!

# So `3` is the last node of this level.

# Add it:

# ```text
# answer = [1, 3]
# ```

# ---

# # Add children

# `3` has right child `4`.

# So:

# ```text
# queue = [4]
# ```

# ---

# # Next level

# ```text
# level_size = 1
# ```

# Take `4`.

# ```text
# i = 0
# ```

# Check:

# ```text
# 0 == 1 - 1
# 0 == 0
# ```

# ✅ Yes.

# Add:

# ```text
# answer = [1, 3, 4]
# ```

# No more nodes.

# Queue:

# ```text
# []
# ```

# So:

# ```python
# while queue:
# ```

# stops.

# Finally:

# ```python
# return answer
# ```

# Returns:

# ```text
# [1, 3, 4]
# ```

# ---

# # 🧠 The whole code in kid language

# Imagine you are standing on the **right side of a tree**.

# You look at the tree **one floor at a time**.

# For every floor:

# ```text
# 1. See how many children are on this floor.
# 2. Check them one by one.
# 3. Keep only the LAST child.
# 4. Put their children in the queue.
# 5. Go to the next floor.
# ```

# So the key pattern is:

# ```text
# BFS
#  ↓
# ONE LEVEL
#  ↓
# LAST NODE
#  ↓
# ANSWER
# ```

# And this line:

# ```python
# if i == level_size - 1:
# ```

# simply means:

# > **"Am I looking at the last node on this floor?"**


        