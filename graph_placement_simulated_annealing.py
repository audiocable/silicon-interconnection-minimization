from collections import defaultdict
import random
import math

def create_adjacency_list(data):
    adjacency_list = defaultdict(list)

    for node, connections in data.items():
        for connected_node in connections:
            adjacency_list[node].append(connected_node)

    return adjacency_list

def calculate_cost(order, adjacency_list):
    cost = 0
    for node, connections in adjacency_list.items():
        for connected_node in connections:
            cost += abs(order.index(node) - order.index(connected_node))
    return cost

def simulated_annealing(nodes, adjacency_list, temperature, cooling_rate):
    current_order = nodes[:]
    current_cost = calculate_cost(current_order, adjacency_list)

    while temperature > 1:
        new_order = current_order[:]
        i, j = random.sample(range(len(nodes)), 2)
        new_order[i], new_order[j] = new_order[j], new_order[i]

        new_cost = calculate_cost(new_order, adjacency_list)

        if new_cost < current_cost or math.exp((current_cost - new_cost) / temperature) > random.random():
            current_order, current_cost = new_order, new_cost

        temperature *= cooling_rate

    return current_order, current_cost

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

initial_temperature = 1000
cooling_rate = 0.995

placement, total_interconnect_length = simulated_annealing(nodes, adjacency_list, initial_temperature, cooling_rate)

print(f"Placement: {placement}")
print(f"Total interconnect length (in terms of unit cell widths): {total_interconnect_length}")