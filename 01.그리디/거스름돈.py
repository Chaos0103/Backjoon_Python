MONEY = 1000
COIN = (500, 100, 50, 10, 5, 1)

price = int(input())

cnt = 0
refund = MONEY - price
for coin in COIN:
    if refund >= coin:
        cnt += refund // coin
        refund %= coin

print(cnt)
