# 深度优先搜索（DFS）实现 - 使用栈（非递归方式）
# Depth-First Search (DFS) implementation - using a stack (non-recursive version)

def dfs_iterative(graph, start):
    # 使用栈来模拟递归过程
    # Use a stack to simulate the recursion process
    stack = [start]

    # 使用集合来记录已访问节点，防止重复遍历
    # Use a set to record visited nodes and avoid repeated visits
    visited = set()

    while stack:
        # 弹出栈顶节点作为当前节点
        # Pop the top node from the stack as the current node
        node = stack.pop()

        if node not in visited:
            # 如果当前节点未访问，则标记为已访问并处理
            # If the current node hasn't been visited, mark it and process it
            print(f"访问节点 Visiting node: {node}")
            visited.add(node)

            # 将所有相邻节点压入栈中（注意：为了保持与递归一致的访问顺序，可逆序推入）
            # Push all neighboring nodes to the stack (reverse to maintain the same order as recursion)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    # 返回所有已访问的节点
    # Return all visited nodes
    return visited


# 示例图结构（使用邻接表表示）
# Example graph structure (represented using an adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 从节点 'A' 开始执行 DFS（非递归版本）
# Execute DFS from node 'A' (iterative version)
dfs_result = dfs_iterative(graph, 'A')
print("DFS 结果 DFS Result:", dfs_result)