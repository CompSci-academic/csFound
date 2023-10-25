import math

def closest_pair_of_points(points):
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def brute_force(points):
        min_distance = float('inf')
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = distance(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    pair = (points[i], points[j])
        return min_distance, pair

    def closest_pair_helper(points_x, points_y):
        n = len(points_x)

        # Base case: if there are 2 or 3 points, use brute force
        if n <= 3:
            return brute_force(points_x)

        mid = n // 2
        midpoint = points_x[mid]

        left_x = points_x[:mid]
        right_x = points_x[mid:]

        left_y = [point for point in points_y if point[0] <= midpoint[0]]
        right_y = [point for point in points_y if point[0] > midpoint[0]]

        # Recursively find closest pairs in left and right subsets
        d1, pair1 = closest_pair_helper(left_x, left_y)
        d2, pair2 = closest_pair_helper(right_x, right_y)

        # Take the minimum of the two closest distances
        min_dist, min_pair = (d1, pair1) if d1 < d2 else (d2, pair2)

        # Check for pairs that are split between the left and right subsets
        strip = [point for point in points_y if abs(point[0] - midpoint[0]) < min_dist]

        # Sort the strip by y-coordinate to efficiently find close pairs
        strip.sort(key=lambda x: x[1])

        # Iterate through the strip and check for closer pairs
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
                dist = distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (strip[i], strip[j])
                j += 1

        return min_dist, min_pair

    # Sort the points by x-coordinate
    points_x = sorted(points, key=lambda x: x[0])
    points_y = sorted(points, key=lambda x: x[1])

    return closest_pair_helper(points_x, points_y)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

min_distance, closest_points = closest_pair_of_points(points)
print("Closest Pair of Points:", closest_points)
print("Minimum Distance:", min_distance)
