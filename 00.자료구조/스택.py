import sys
N = int(input())
stack = []
idx = -1
for _ in range(N):
    data = list(sys.stdin.readline().split())
    if data[0] == 'push':
        stack.append(int(data[1]))
        idx += 1
    elif data[0] == 'pop':
        if idx == -1:
            print(-1)
        else:
            print(stack[idx])
            del stack[idx]
            idx -= 1
    elif data[0] == 'size':
        print(len(stack))
    elif data[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif data[0] == 'top':
        if idx == -1:
            print(-1)
        else:
            print(stack[idx])
