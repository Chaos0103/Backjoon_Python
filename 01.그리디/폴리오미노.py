ch = input()

result = list()
cnt = 0
idx = 0
idx_cnt = 0
TF = True

for c in ch:
    if c != '.':
       cnt += 1
    if c == '.' or idx_cnt + 1 == len(ch):
        if cnt % 4 == 0:
            for i in range(idx, idx + cnt):
                result.append('A')
        elif cnt % 4 == 2:
            for i in range(idx, idx + cnt - 2):
                result.append('A')
            result.append('B')
            result.append('B')
        else:
            TF = False
            break
        result.append('.')
        idx = ch.index(c) + 1
        cnt = 0
    idx_cnt += 1

if TF:
    for i in range(len(ch)):
        print(result[i], end='')
else:
    print(-1)
