import sys
input = sys.stdin.readline


def binary_search(arr, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return True


N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if binary_search(A, i, 0, N - 1):
        print(1)
    else:
        print(0)
        
# pypy 제출
# 2줄 처럼 명령을 바꿀 수 있음
