from collections import deque
import copy

N, M = map(int, input().split())  # N은 큐의 크기, M은 뽑아내려는 수의 개수
# 뽑아내려고 하는 수의 위치 (순서대로) (1~N 범위)
location_list = list(map(int, input().split()))

# 목표: 원소를 주어진 순서대로 뽑아내는 데 드는 2번, 3번 연산의 최솟값
result_cnt = 0
# 1번 연산: 첫 원소를 뽑아낸다. queue.popleft()  -> M개만 뽑을 수 있음.
# 2번 연산: 왼쪽으로 한 칸 민다. queue.rotate(-1)
# 3번 연산: 오른쪽으로 한 칸 민다. queue.rotate(1)

dq1 = deque(range(1, N+1))  # 크기 N인 deque 생성. 숫자는 위치를 의미함.
dq2 = copy.deepcopy(dq1)  # 왼쪽, 오른쪽 2번 돌려보기 위해 2개 생성

for num in location_list:  # 뽑으려는 수의 위치 순서대로 꺼내기
    # 왼쪽으로 이동하는 경우와 오른쪽으로 이동하는 경우 각각 구해 최솟값 선택해 이동.
    left_cnt = 0
    right_cnt = 0
    while dq1[0] != num: # 찾는 숫자가 맨 앞에 올 때까지 왼쪽으로 한 칸씩 회전
        dq1.rotate(-1)
        left_cnt += 1
    while dq2[0] != num:  # 오른쪽을 회전
        dq2.rotate(1)
        right_cnt += 1
    if left_cnt < right_cnt:  # 더 작은 값으로 채택
        result_cnt += left_cnt
        dq1.popleft()  # 맨 앞 원소 뽑아내기
        dq2 = copy.deepcopy(dq1)
    else:
        result_cnt += right_cnt
        dq2.popleft()  # 맨 앞 원소 뽑아내기
        dq1 = copy.deepcopy(dq2)

print(result_cnt)