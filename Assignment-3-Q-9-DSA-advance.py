from collections import deque

def maxLevelSum(root):
    if not root:
        return 0

    maxSum = float('-inf')
    queue = deque([root])

    while queue:
        currentLevelSum = 0
        currentLevelCount = 0

        for _ in range(len(queue)):
            node = queue.popleft()
            currentLevelSum += node.val
            currentLevelCount += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if currentLevelSum > maxSum:
            maxSum = currentLevelSum

    return maxSum