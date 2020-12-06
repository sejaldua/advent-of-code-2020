import re

"""
REQUIRED FIELDS:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
def puzzle1():
    res = 0
    with open("input.txt", 'r') as file:
        l = file.read().split('\n\n')
        for s in l:
            if s != "":
                text = s.split()
                passport = dict()
                for field in text:
                    k, v = field.split(":")
                    passport[k] = v
                if all([field in passport.keys() for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]):
                    res += 1
    return res


"""
CRITERIA:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
"""
def puzzle2():
    rules = {
        'byr': (lambda x: True if int(x) >= 1920 and int(x) <= 2002 else False),
        'iyr': (lambda x: True if int(x) >= 2010 and int(x) <= 2020 else False), 
        'eyr': (lambda x: True if int(x) >= 2020 and int(x) <= 2030 else False), 
        'hgt': (lambda x: True if ("cm" in x and int(x[:x.find("cm")]) >= 150 and int(x[:x.find("cm")]) <= 193) or ("in" in x and int(x[:x.find("in")]) >= 59 and int(x[:x.find("in")]) <= 76) else False),
        'hcl': (lambda x: True if len(x) == 7 and re.match("^#([a-f0-9]{6})", x) else False),  
        'ecl': (lambda x: True if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False), 
        'pid': (lambda x: True if len(x) == 9 and int(x) else False)
    }
    res = 0
    with open("input.txt", 'r') as file:
        l = file.read().split('\n\n')
        for s in l:
            if s != "":
                text = s.split()
                passport = dict()
                for field in text:
                    k, v = field.split(":")
                    passport[k] = v
                checks = {key: rules[key](value) for key, value in passport.items() if key in ['byr', 'iyr', 'eyr', 'hcl', 'hgt', 'ecl', 'pid']}
                if all([field in passport.keys() for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]) and all(checks.values()):
                    res += 1
    return res

if __name__ == "__main__":
    print(puzzle1())
    print(puzzle2())