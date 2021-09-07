N, K = map(int, input().split())
coin = list()

for _ in range(N):
    a = int(input())
    coin.append(a)

coin.sort(reverse=True)
cnt = 0
for c in coin:
    if K == 0:
        break
    if K // c == 0:
        continue
    cnt += K//c
    K %= c

print(cnt)
