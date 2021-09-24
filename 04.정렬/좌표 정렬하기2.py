import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
data = sorted(data)
data = sorted(data, key = lambda a: a[1])

for i in data:
    print(i[0], i[1])
