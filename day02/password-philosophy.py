def puzzle1(fin):
    with open(fin, 'r') as file:
        l = file.read().split('\n')[:-1]
    valid = 0
    for line in l:
        lo = int(line.split('-')[0])
        hi = int(line.split('-')[1][:line.split('-')[1].find(' ')])
        letter = line[line.find(":")-1]
        pwd = line.split(": ")[1]
        count = 0
        for char in pwd:
            if char == letter:
                count += 1
        if count >= lo and count <= hi:
            valid += 1
    return valid


def puzzle2(fin):
    with open(fin, 'r') as file:
        l = file.read().split('\n')[:-1]
    valid = 0
    for line in l:
        lo = int(line.split('-')[0])
        hi = int(line.split('-')[1][:line.split('-')[1].find(' ')])
        letter = line[line.find(":")-1]
        pwd = line.split(": ")[1]
        try:
            if (pwd[lo-1] == letter) ^ (pwd[hi-1] == letter):
                valid += 1
        except:
            continue
    return valid

if __name__ == "__main__":
    print(puzzle1("input.txt"))
    print(puzzle2("input.txt"))