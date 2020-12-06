
def get_boarding_passes():
    with open("input.txt", 'r') as file:
        return file.read().split('\n')[:-1]
    
def binary_search(s, lo, hi):
    for char in s:
        if char == "F" or char == "L":
            hi -= (hi - lo) // 2 + 1
        else:
            lo += (hi - lo) // 2 + 1
    return lo if char == "F" or char == "L" else hi

def bitwise_binary_search(l):
    return [int(x.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), base=2) for x in l]

def get_seat_ids(l):
    return [binary_search(s[:7], 0, 127) * 8 + binary_search(s[7:], 0, 7) for s in l]

def puzzle1():
    l = get_boarding_passes()
    seat_ids = get_seat_ids(l)
    # seat_ids = bitwise_binary_search(l)
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