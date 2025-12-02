T = int(input())

def func(n):
    if n < 3:
        return n
    elif n == 3:
        return 4
    return func(n-1) + func(n-2) + func(n-3)

for _ in range(T):
    n = int(input())
    # 목표: 양의 정수 n을 1, 2, 3의 합으로 나타내는 방법의 수
    # f(n-1)에 1을 더한 것 1종류 f(n-1)
    # f(n-2)에 2를 더한것 1종류. f(n-2)
    # f(n-3)에 3을 더한 것 1종류 f(n-3)


    print(func(n))