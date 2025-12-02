from collections import deque

N, K = map(int, input().split())
# 1~N 까지 N명의 사람
# K번째 사람 제거. 남은 사람들로 반복. 모두 제거될 때까지 계속.
# 목표: 요세푸스 순열(원에서 사람들이 제거되는 순서) 출력
dq = deque(list(range(1, N+1)))  # rotate와 popleft 활용하기 위해 deque 자료구조 선택

dq.rotate()
