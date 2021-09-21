import sys
from collections import deque
N = int(input())
queue = deque()
for _ in range(N):
    data = list(sys.stdin.readline().split())
    if data[0] == 'push_front':
        queue.appendleft(int(data[1]))
    elif data[0] == 'push_back':
        queue.append(int(data[1]))
    elif data[0] == 'pop_front':
        if len(queue):
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif data[0] == 'pop_back':
        if len(queue):
            print(queue[len(queue) - 1])
            queue.pop()
        else:
            print(-1)
    elif data[0] == 'size':
        print(len(queue))
    elif data[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif data[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif data[0] == 'back':
        if len(queue):
            print(queue[len(queue) - 1])
        else:
            print(-1)
