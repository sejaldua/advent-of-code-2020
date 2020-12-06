
def binary_search(s, lo, hi):
    for char in s:
        if char == "F" or char == "L":
            hi -= (hi - lo) // 2 + 1
        else:
            lo += (hi - lo) // 2 + 1
    return lo if char == "F" or char == "L" else hi

def puzzle1():
    seat_ids = []
    with open("input.txt", 'r') as file:
        l = file.read().split('\n')[:-1]
        for s in l:
            row = binary_search(s[:7], 0, 127)
            col = binary_search(s[7:], 0, 7)
            seat_id = row * 8 + col
            seat_ids.append(seat_id)
    return seat_ids

def puzzle2():
    seat_ids = puzzle1()
    missing = [i for i in range(max(seat_ids)) if i not in seat_ids]
    for x in missing:
        if (x - 1) not in missing and (x + 1) not in missing:
            return x

if __name__ == "__main__":
    print(max(puzzle1()))
    print(puzzle2())