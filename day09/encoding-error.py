def get_input():
    with open("input.txt", 'r') as file:
        return [int(line.strip()) for line in file.read().strip().split("\n")]

def check_sum(target, arr):
    for i, first in enumerate(arr):
        if first <= target:
            for second in arr[i:]:
                if first + second == target:
                    return True
    return False

def puzzle1():
    numbers = get_input()
    preamble = numbers[:25]
    numbers = numbers[25:]
    for i, num in enumerate(numbers):
        if not check_sum(num, preamble): return num
        preamble = preamble[1:] + [num]
    return -1

def get_contiguous(target, numbers):
    seq = []
    for num in numbers:
        if sum(seq) + num < target:
            seq.append(num)
        elif len(seq) >= 2 and sum(seq) + num == target:
            seq.append(num)
            return min(seq) + max(seq)
        else:
            return get_contiguous(target, numbers[1:])

def puzzle2():
    target = puzzle1()
    numbers = get_input()
    return get_contiguous(target, numbers)

if __name__ == "__main__":
    print(puzzle1())
    print(puzzle2())