# The "What" (최종 코드)

n, x = map(int, input().split())
data = list(map(int, input().split()))

for num in data:
    if num < x:
        print(num, end=' ')