from collections import defaultdict

def create_adjacency_list(data):
    adjacency_list = defaultdict(list)

    for node, connections in data.items():
        for connected_node in connections:
            adjacency_list[node].append(connected_node)

    return adjacency_list

def find_longest_interconnection(nodes, adjacency_list):
    unplaced_nodes = set(nodes)
    placed_nodes = []

    while unplaced_nodes:
        min_longest_interconnect = float('inf')
        best_node = None
        best_position = None

        for node in unplaced_nodes:
            for position in range(len(placed_nodes) + 1):
                temp_placement = list(placed_nodes[:position] + [node] + placed_nodes[position:])
                longest_interconnect = 0

                for i, n1 in enumerate(temp_placement):
                    for n2 in adjacency_list[n1]:
                        if n2 in temp_placement:
                            longest_interconnect = max(longest_interconnect, abs(i - temp_placement.index(n2)))

                if longest_interconnect < min_longest_interconnect:
                    min_longest_interconnect = longest_interconnect
                    best_node = node
                    best_position = position

        placed_nodes.insert(best_position, best_node)
        unplaced_nodes.remove(best_node)

    longest_interconnect = 0
    for i, n1 in enumerate(placed_nodes):
        for n2 in adjacency_list[n1]:
            if n2 in placed_nodes:
                longest_interconnect = max(longest_interconnect, abs(i - placed_nodes.index(n2)))

    return placed_nodes, longest_interconnect

# Input data
data = {
    1: [2, 3, 4],
    2: [1, 3, 4, 5],
    3: [1, 2, 6],
    4: [1, 2, 5, 8],
    5: [2, 4, 6, 7],
    6: [3, 5],
    7: [5, 8, 9, 10, 11, 12, 15],
    8: [4, 7, 10, 11, 13],
    9: [7, 12, 14],
    10: [7, 8, 11, 14],
    11: [7, 8, 10, 12, 13],
    12: [7, 9, 11, 14],
    13: [8, 11, 14, 15],
    14: [9, 10, 12, 13, 15],
    15: [7, 13, 14]
}

adjacency_list = create_adjacency_list(data)
nodes = list(adjacency_list.keys())

placement, longest_interconnect = find_longest_interconnection(nodes, adjacency_list)

print(f"Placement: {placement}")
print(f"Longest interconnect length (in terms of unit cell widths): {longest_interconnect}")