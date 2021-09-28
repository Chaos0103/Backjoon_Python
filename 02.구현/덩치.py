import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

s = sorted(data, reverse=True)

for i in range(n):
    rank = 1
    for j in range(n):
        if data[i][0] < s[j][0] and data[i][1] < s[j][1]:
            rank += 1
    print(rank, end=' ')
