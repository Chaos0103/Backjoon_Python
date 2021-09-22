import sys
N = int(sys.stdin.readline())

data = []

for _ in range(N):
    data.append(int(sys.stdin.readline()))

result = sorted(data)

for i in result:
    print(i)
   
# sort()보다 sorted()가 더 빠름
# 입력 속도를 위해서 sys를 습관화 할 것
