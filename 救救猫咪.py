def get_points(points):
    n = len(points)
    result = [0]*n
    for i in range(n):
        count = 0
        x1,y1 = points[i]
        for j in range(n):
            if j != i:
                x2, y2 = points[j]
                if x1 < x2 and y1 < y2:
                    count += 1
        result[i] = count
    return result
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
for count in get_points(points):
    print(count)