n = int(input())  # n은 정수의 개수
# 1부터 n까지의 수를 스택으로 넣었다가 뽑아 늘어놓음으로써 하나의 수열을 만든다.
arr = [int(input()) for _ in range(n)]  # 주어진 수열

stack = [0] * n  # stack 초기화
top = -1
num = 1  # 스택에 쌓을 숫자

# 결과를 한 번에 출력하기 위해 리스트를 만든다.
result = []

for idx in range(n):
    while arr[idx] > stack[top]:  # 수열의 숫자가, 스택의 top 값보다 크면, 스택을 더 쌓는다.
        top += 1  # push
        stack[top] = num
        num += 1
        result.append('+')
    if arr[idx] == stack[top]:  # 수열의 숫자가, 스택의 top 값과 같으면, pop한다.
        top -= 1  # pop
        result.append('-')
    if arr[idx] < stack[top]:  # 수열의 숫자가, 스택의 top 값보다 작으면, 수열을 만들 수 없다.
        result = ['NO']
        break  # for idx 종료

for item in result:
    print(item)