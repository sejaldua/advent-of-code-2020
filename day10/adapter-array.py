def get_input():
    with open("input.txt", 'r') as file:
        return [int(line.strip()) for line in file.read().strip().split("\n")]

def puzzle1():
    joltage_ratings = get_input()
    numbers = [0] + sorted(joltage_ratings) + [max(joltage_ratings) + 3]
    jolt_differences = {1: 0, 3: 0}
    for i in range(1, len(numbers)):
        jolt_differences[numbers[i] - numbers[i-1]] += 1
    return jolt_differences[1] * jolt_differences[3]

# dynamic programming approach
def puzzle2():
    joltage_ratings = get_input()
    numbers = [0] + sorted(joltage_ratings) + [max(joltage_ratings) + 3]
    dp = [0]*len(numbers)
    dp[len(numbers)-1] = 1
    for i in reversed(range(len(numbers)-1)):
        try:
            for j in range(1,4):
                if numbers[i+j] - numbers[i] <= 3:
                    dp[i] += dp[i+j]
        except:
            continue
    return dp[0] 

if __name__ == "__main__":
    print(puzzle1())
    print(puzzle2())