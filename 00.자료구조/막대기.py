import sys
N = int(sys.stdin.readline())
stick = list()

for _ in range(N):
    var = int(sys.stdin.readline())
    stick.append(var)

stick.reverse()
height = stick[0]
cnt = 1

for var in stick:
    if height < var:
        cnt += 1
        height = var

print(cnt)
