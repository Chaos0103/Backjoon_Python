COIN = (25, 10, 5, 1)

case = int(input())

for _ in range(case):
    cent = int(input())
    coin_cnt = [0] * 4
    idx = 0
    for coin in COIN:
        if cent >= coin:
            coin_cnt[idx] = (cent // coin)
            cent %= coin
        idx += 1
    for i in range(4):
        print(coin_cnt[i], end=' ')
    print('')
