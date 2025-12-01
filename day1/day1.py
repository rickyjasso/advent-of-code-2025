def main():
    directions = []
    amounts = []
    with open("input.txt") as f:
        for line in f:
            directions.append(line[0])
            amounts.append(int(line[1:-1]))
    
    number = 50
    count = 0
    clicks = 0
    for i in range(len(directions)):
        for j in range(amounts[i]):
        # move 1 step at a time, if we ever 'click', add that to the clicks counter
            if directions[i] == 'L':
                number = (number - 1 + 100) % 100
            elif directions[i] == 'R':
                number = (number+1) % 100
            if number == 0:
                clicks += 1
        # if after all the movement, we land at 0, add to the count (part 1)
        if number == 0:
            count +=1
    print(count)
    print(clicks)

if __name__ == "__main__":
    main()
