def sum_of_nodes(height):
    total_nodes = 2**(height+1) - 1
    first_node_value = 1
    last_node_value = total_nodes
    node_sum = (total_nodes * (first_node_value + last_node_value)) // 2
    return node_sum

# Example usage:
height = 3
sum = sum_of_nodes(height)
print("Sum of all nodes in the perfect binary tree:", sum)
