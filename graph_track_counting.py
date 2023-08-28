def count_tracks(placement, data):
    tracks = [0] * len(placement)
    
    for i, node1 in enumerate(placement):
        for node2 in data[node1]:
            if node2 in placement[i+1:]:
                j = placement.index(node2)
                track = max(tracks[i], tracks[j]) + 1
                tracks[j] = track
                
    return max(tracks)

def find_placement(data):
    unplaced_nodes = sorted(data.keys(), key=lambda x: len(data[x]), reverse=True)
    placement = []

    while unplaced_nodes:
        node = unplaced_nodes.pop(0)
        placement.append(node)

    return placement

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

placement = find_placement(data)
tracks_required = count_tracks(placement, data)

print("Placement:", placement)
print("Number of tracks required:", tracks_required)