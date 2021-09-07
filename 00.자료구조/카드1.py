card_cnt = int(input())

if card_cnt == 1:
    print(1)
else:
    card = [num + 1 for num in range(card_cnt)]
    idx = 0
    while True:
        print(card[idx], end=' ')
        idx += 1
        card.append(card[idx])
        idx += 1
        if idx == len(card)-1:
            print(card[idx])
            break
