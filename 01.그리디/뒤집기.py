str_num = input()
cnt = 1

for idx in range(1, len(str_num)):
    if str_num[idx - 1] != str_num[idx]:
        cnt += 1

print(cnt // 2)
