N = int(input())
data = []
while N != 0:
    data.append(N % 10)
    N //= 10

data.sort(reverse=True)

for i in data:
    print(i, end='')
