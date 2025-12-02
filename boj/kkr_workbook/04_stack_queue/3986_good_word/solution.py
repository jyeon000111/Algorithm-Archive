N = int(input())  # 단어의 수
# A끼리 B끼리 짝을 지었을 때, 서로 교차하지 않으면 좋은 단어 (괄호 문제와 동일)
# 목표: 좋은 단어의 수
result_cnt = 0
for _ in range(N):
    word = input()  # A와 B로 이루어진 단어
    # 홀수면 좋은 단어가 될 수 없다.
    if len(word) % 2 == 1:
        continue

    stack = []
    for char in word:
        # 스택이 비었거나, 스택의 마지막 원소가 같은 원소가 아니면 push
        if (not stack) or (stack[-1] != char):
            stack.append(char)
        # 스택의 마지막 원소가 같은 원소면 pop
        elif stack[-1] == char:
            stack.pop()

    # 스택에 값이 남았으면 좋은 단어가 아니다.
    if stack:
        continue

    result_cnt += 1

print(result_cnt)