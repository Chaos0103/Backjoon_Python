import sys

N = int(sys.stdin.readline())
count = [0]*(10001)
for _ in range(N):
    data = int(sys.stdin.readline())
    count[data] += 1


for i in range(len(count)):
    if(count[i] != 0):
        for j in range(count[i]):
            print(str(j))

# sys.stdout.write가 print보다 메모리 효율면에서 좋은가?
