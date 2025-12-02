K = int(input())
stack = []
for _ in range(K):  # K개의 줄에 정수 1개씩 주어짐
    num = int(input())
    # 목표: 입력받은 정수의 합. '0' 입력 시 가장 최근에 쓴 수 pop
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))