from collections import deque

N = int(input())  # 1~N 번호 카드 (1번이 제일 위)

queue = deque(range(N, 0, -1))  # 제일 위 카드가 오른쪽 끝

while len(queue) > 1:
    # 제일 위 카드를 버린다.
    queue.pop()
    # 제일 위 카드를 제일 아래(왼쪽 끝)로 옮긴다.
    queue.appendleft(queue.pop())

print(queue[0])
