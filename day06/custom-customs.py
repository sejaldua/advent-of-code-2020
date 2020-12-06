
def get_input():
    with open("input.txt", 'r') as file:
        input = file.read()
        groups = input.split('\n\n')
        return [[answers for answers in group.split("\n")] for group in groups]
    
def puzzle1():
    groups = get_input()
    return sum([len(set("".join(g))) for g in groups])    

def puzzle2():
    groups = get_input()
    res = 0
    for group in groups:
        for i, answers in enumerate(group):
            curr = set(answers) if i == 0 else curr.intersection(set(answers))
        res += len(curr)
    return res

if __name__ == "__main__":
    print(puzzle1())
    print(puzzle2())