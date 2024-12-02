# Part 1
first = []
second = []

with open(b"C:\Users\smitt\OneDrive\Documents\AOC 2024/aoc-2024\data-day-1.txt", 'r') as file:
    for line in file:
        first.append(line.split()[0])
        second.append(line.split()[1])

first.sort()
second.sort()

distance = 0
for x, y in zip(first, second):
    temp = abs(int(x) - int(y))
    distance += temp

print(distance)

# Part 2
distance2 = 0
for x in first:
    count = 0
    for y in second:
        if x == y:
            count += 1
    distance2 += (int(x) * count)

print(distance2)
