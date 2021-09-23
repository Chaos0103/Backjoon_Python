import sys

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    ch = sys.stdin.readline().rstrip()
    data.append(ch)

result = sorted(data)
before = ''
for i in range(1, 51):
    for c in result:
        if len(c) == i:
            if before == c:
                continue
            else:
                before = c
                print(c)
