class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            self.parent[pi] = pj

def kruskals_algorithm(door_pairs, num_rooms):
    # Initialize UnionFind
    uf = UnionFind(num_rooms)

    # Sort the door pairs based on distance
    door_pairs.sort(key=lambda x: x[2])

    mst = []

    for door_a, door_b, dist in door_pairs:
        # Find the root ancestors of the rooms to which doors belong
        root_a = uf.find(door_a.room_id)
        root_b = uf.find(door_b.room_id)

        # If they belong to different sets, union them and add to MST
        if root_a != root_b:
            uf.union(root_a, root_b)
            mst.append((door_a, door_b, dist))

    return mst
