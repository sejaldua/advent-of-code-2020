def puzzle1(fin):
    with open(fin, 'r') as file:
        l = file.read().split('\n')
        arr = [[char for char in s] for s in l if s != ""]
    x = 0
    tree_count = 0
    for y in range(1, len(arr)):
        x = (x + 3) % len(arr[0])
        if arr[y][x] == "#":
            tree_count += 1
    return tree_count


def puzzle2(fin):
    with open(fin, 'r') as file:
        l = file.read().split('\n')
        arr = [[char for char in s] for s in l if s != ""]
    tree_counts = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        tree_count = 0
        x = 0
        y = 0
        while y < len(arr) - 1:
            x = (x + slope[0]) % len(arr[0])
            y += slope[1]
            if arr[y][x] == "#":
                tree_count += 1
        tree_counts.append(tree_count)
    res = 1
    for tc in tree_counts:
        res *= tc
    return res

if __name__ == "__main__":
    print(puzzle1("input.txt"))
    print(puzzle2("input.txt"))