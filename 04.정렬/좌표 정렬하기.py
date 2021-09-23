import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

result = sorted(data)

for i in result:
    print(i[0], i[1])
