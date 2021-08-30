cnt = 1
while True:
    L, P, V = map(int, input().split())
    
    if L == 0 and P == 0 and V == 0:
        break
    num = V % P
    if num > L:
        num = L
    result = L * (V // P) + num
    print(f'Case {cnt}: {result}')
    cnt += 1
