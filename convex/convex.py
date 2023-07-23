def unit_dist_pairs(pts):
    # Sort points based on x-coordinate
    sorted_pts = sorted(pts, key=lambda p: p[0])

    # Split the sorted points into two monotonic sequences based on y-coordinate
    mid_idx = len(sorted_pts) // 2
    first_seq = sorted_pts[:mid_idx]
    second_seq = sorted_pts[mid_idx:]

    # Function to find the points with y-coordinate exactly one unit distance away
    def matching_pts(sequence, y):
        return [p for p in sequence if abs(p[1] - y) == 1]

    unit_dist_pairs = []

    # Find pairs from first_seq to second_seq
    for x, y in first_seq:
        matches = matching_pts(second_seq, y)
        unit_dist_pairs.extend([(x, mx) for mx, my in matches])

    # Find pairs from second_seq to first_seq
    for x, y in second_seq:
        matches = matching_pts(first_seq, y)
        unit_dist_pairs.extend([(x, mx) for mx, my in matches])

    return unit_dist_pairs

# Example usage:
points = [(1, 2), (2, 3), (3, 3), (4, 2), (5, 1), (6, 1)]
pairs = unit_dist_pairs(points)
print(pairs)

# Overall Time Complexity: O(nlog(n)) + O(n) + 2(O(n^2)) ≈ O(n^2) (dominated by the two loops)

# Overall Space Complexity: O(n) (for the intermediate lists sorted_pts, first_seq, and second_seq) + O(k) (where k is the number of unit distance pairs) ≈ O(n)

