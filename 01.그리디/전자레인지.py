TIME = (300, 60, 10)
time_cnt = [0] * 3

make_time = int(input())

for idx in range(3):
    if make_time >= TIME[idx]:
        time_cnt[idx] += (make_time // TIME[idx])
        make_time %= TIME[idx]

if make_time == 0:
    print(time_cnt[0], time_cnt[1], time_cnt[2])
else:
    print(-1)
