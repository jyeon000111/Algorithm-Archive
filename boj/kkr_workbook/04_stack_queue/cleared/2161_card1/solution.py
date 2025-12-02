N = int(input())  # 1~N 번호가 붙은 카드 N장. (1번이 제일 위, N번이 제일 아래)
# 카드 1장 남을 때까지 반복
# 1. 제일 위의 카드를 버린다.
# 2. 제일 위의 카드를 맨 밑으로 옮긴다.
# 목표: 버린 카드 순서대로 출력. 마지막 카드 출력

stack = [num for num in range(N, 0, -1)]  # 오른쪽 끝 카드가 제일 위의 카드. [아래 ~ 위]

while len(stack) > 1:
    print(stack.pop(), end=' ')
    stack.insert(0, stack.pop())

print(*stack)
