import sys

def find_repeated_substring(number):
    suffix_arr = [int(number[i:]) for i in range(len(number))]
    suffix_arr = sorted(suffix_arr[1:])
    invalid_id = 0
    
    for sfx in suffix_arr:
        if len(number) % len(str(sfx)) != 0:
            continue
        substr = str(sfx)
        l = 0
        success = True
        while l < len(substr):
            if substr[l] != number[l]:
                success = False
                break
            l+=1
        if success:
            l2 = 0
            while l2 < len(number):
                if number[l2:l2+l] != substr:
                    success = False
                    break
                l2 += l
        if success:
            invalid_id += int(number)
            break

    return invalid_id

def get_invalid_ids(input):
    input = input.strip().split(",")
    ranges = []
    result = 0
    repeated = 0

    for l in input:
        s = l.split("-")
        ranges.append((s[0], s[1]))

    for r in ranges:
        min = int(r[0])
        max = int(r[1])
        for i in range(min, max+1):
            comparable_i = str(i)
            invalid_id = find_repeated_substring(comparable_i)
            if invalid_id != 0:
                result+= invalid_id
                continue
            if len(comparable_i) % 2 == 0:
                l = 0
                r = len(comparable_i) // 2
                success = True
                while r < len(comparable_i):
                    if comparable_i[l] != comparable_i[r]:
                        success = False
                        break
                    l+=1
                    r+=1
                if success:
                    result += i
    return result + repeated

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 day2.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    f = open(file_path)
    input = f.read()

    result = get_invalid_ids(input)
    print(result)

if __name__ == "__main__":
    main()
