from collections import deque

N, K = map(int, input().split())
# 1~N 번까지 N명의 사람이 원을 이루며 앉아 있다.
# 순서대로 K번째 사람 제거
# 목표: 원에서 사람들이 제거되는 순서(요세푸스 순열) 출력
dq = deque(list(range(1, N+1)))
# 규칙: 왼쪽으로 K-1 칸 회전시키고 맨 앞 제거하고, 순열에 추가
result = []
while dq:  # dq가 텅 빌 때까지 반복
    dq.rotate(-(K-1))  # K-1 칸 회전
    result.append(dq.popleft())

print('<', end='')
# 출력을 위해 str로 변경
result = list(map(str, result))
print(', '.join(result), end='')
print('>')
