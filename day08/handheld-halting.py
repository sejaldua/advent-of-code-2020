def get_input():
    with open("input.txt", 'r') as file:
        return [line.strip() for line in file.read().strip().split("\n")]

def get_next_instruction(instruction, idx, acc):
    instr, num = instruction.split(" ")
    if instr == "acc":
        acc += int(num)
        idx += 1
    elif instr == "jmp":
        idx += int(num)
    else:
        idx += 1
    return idx, acc

def run(lines):
    idx, acc = 0, 0
    record = [0]*len(lines)
    while idx < len(lines):
        if record[idx] == 1:
            return acc, False
        else:
            record[idx] = 1
            idx, acc = get_next_instruction(lines[idx], idx, acc)
    return acc, True

def puzzle1():
    lines = get_input()
    acc, _ = run(lines)
    return acc

def puzzle2():
    lines = get_input()
    for i, line in enumerate(lines):
        mod_lines = lines.copy()
        instr, num = line.split(" ")
        if instr == "jmp":
            mod_lines[i] = line.replace("jmp", "nop")
        elif instr == "nop":
            mod_lines[i] = line.replace("nop", "jmp")
        acc, terminated = run(mod_lines)
        if terminated:
            return acc

if __name__ == "__main__":
    print(puzzle1())
    print(puzzle2())