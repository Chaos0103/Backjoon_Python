import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    data.append((int(age), name))

data = sorted(data, key = lambda age: age[0])

for i in data:
    print(i[0], i[1])
