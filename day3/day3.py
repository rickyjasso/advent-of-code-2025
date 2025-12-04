import sys

def total_output_joltage(contents):
    total_joltage = 0
    total_joltage_p2 = 0
    for line in contents:
        total_joltage += find_largest_joltage(line, 2)
        total_joltage_p2 += find_largest_joltage(line, 12)
    return total_joltage, total_joltage_p2

def find_largest_joltage(input, num_batteries):
    start = 0
    end = len(input) - num_batteries
    joltage = 0
    for i in range(num_batteries):
        window = input[start:end+1]
        index = window.index(max(window))
        joltage += (int(window[index]) * (10 ** (num_batteries - i - 1)))
        start = start + index + 1
        end += 1
    return joltage

'''
--- BRUTE FORCE SOLUTION ---
def find_largest_joltage(input):
    num_digits = len(input)
    str_nums = str(input)
    joltage = 0
    for i in range(num_digits):
        for j in range(i+1, num_digits):
            joltage = max(joltage, int(input[i]+input[j]))
    return joltage
'''

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 day3.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        contents = f.readlines()

    contents = [line.strip() for line in contents]
    p1, p2 = total_output_joltage(contents)
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()

