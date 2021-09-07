seat = int(input())
position = input()

hole = ['*']
couple = False
for pos in position:
    hole.append(pos)
    if pos == 'L' and not(couple):
        couple = True
        continue
    elif couple:
        couple = False
    hole.append('*')

cnt = 0
for idx in range(len(hole)):
    if hole[idx] == '*' or hole[idx] == 'C':
        continue
    if hole[idx-1] == '*':
        hole[idx-1] = 'C'
        cnt += 1
    elif hole[idx+1] == '*':
        hole[idx+1] = 'C'
        cnt += 1

print(cnt)
