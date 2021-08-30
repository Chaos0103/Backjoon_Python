width, basket = map(int, input().split())
apple = int(input())

basket_right = basket
basket_left = 1
cnt = 0
for _ in range(apple):
    point = int(input())

    if basket_left <= point <= basket_right:
        continue
    else:
        if point < basket_left:
            dif = basket_left - point
            basket_left -= dif
            basket_right -= dif
            cnt += dif
        else:
            dif = point - basket_right
            basket_left += dif
            basket_right += dif
            cnt += dif

print(cnt)
