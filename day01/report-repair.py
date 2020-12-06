def puzzle1(fin):
    with open(fin, 'r') as file:
        l = file.read().split('\n')
        l = [int(s) for s in l if s != ""]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[i] + l[j] == 2020:
                return l[i] * l[j]

def puzzle2(fin):
    with open(fin, 'r') as file:
        l = file.read().split('\n')
        l = [int(s) for s in l if s != ""]
    for i in range(len(l)):
        for j in range(i, len(l)):
            for k in range(j, len(l)):
                if l[i] + l[j] + l[k] == 2020:
                    return l[i] * l[j] * l[k]

if __name__ == "__main__":
    print(puzzle1("input.txt"))
    print(puzzle2("input.txt"))