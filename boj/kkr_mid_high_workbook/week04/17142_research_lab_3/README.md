## 1. 문제 정보 (Problem)

  - **문제 이름**: 연구소 3
  - **출처 및 번호**: [백준 17142]('https://www.acmicpc.net/problem/17142')
  - **난이도**: 골드 3
  - **문제 요약**: 연구소의 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간 구하기

---
## 2. 핵심 아이디어 (Core Logic)


---
## 3. 어려웠던 점 (Difficulties)


---
## 4. 새롭게 배운 점 (What I Learned)



---
## 5. 코드 개선 (Refactoring)
### 초기 코드
```python
def bfs(start_indices, blank):
    '''
    활성화 바이러스 M개의 출발점을 담은 튜플과 감염시킬 빈칸 수를 인자로 받아,
    모든 빈칸을 감염시킬 때까지 소요되는 최소 시간을 구해 반환합니다.
    탐색 끝나도 모두 감염시키지 못한 경우 False를 반환합니다.
    BFS 로 탐색합니다.
    '''
    global min_ans

    dq = deque(list(start_indices))
    
    # 방문 여부 및 소요 시간 기록할 배열 복사
    cur_matrix = [row[:] for row in lab_matrix]  # 얕은 복사 (깊은 복사 불필요. deepcopy는 오버헤드 커짐)
    # 시작점 방문 표시
    for start_y, start_x in start_indices:
        cur_matrix[start_y][start_x] = 0

    
    while dq:
        now_y, now_x = dq.popleft()
        now_time = cur_matrix[now_y][now_x]

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
            next_y = now_y + dy
            next_x = now_x + dx
            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N:  # 인덱스 범위 체크
                continue

            if cur_matrix[next_y][next_x] in ('#', '*'):  # 빈칸 또는 비활성인 경우만 복제
                if cur_matrix[next_y][next_x] == '#':  # 빈칸인 경우, 잔여 빈칸 수 차감
                    blank -= 1
                cur_matrix[next_y][next_x] = now_time + 1  # 방문 및 소요시간 표시
                dq.append((next_y, next_x))  # 인큐

            if blank == 0:  # 모두 감염시켰으면, 소요된 최소 시간 반환
                cur_min = now_time + 1
                return cur_min

    # 빈칸 남은 채로 탐색이 끝났다면 False 반환
    return False





N, M = list(map(int, input().split()))  # N은 연구소 배열 크기, M은 활성 전환할 바이러스 개수

lab_matrix = [list(map(int, input().split())) for _ in range(N)]  # N*N 연구소 상태
# 0은 빈칸, 1은 벽, 2는 비활성 바이러스의 위치 

# 비활성 바이러스 인덱스(출발점 후보), 감염시켜야 할 칸 수 구해두기
# + 빈칸(#), 벽(-), 비활성 바이러스(*) 하기 (맵에 소요시간 기록하기 위해, 숫자 아닌 기호로 표시)
inactivated_virus = [] 
blank_cnt = 0

for row_idx in range(N):
    for col_idx in range(N):
        if lab_matrix[row_idx][col_idx] == 0:  # 빈칸
            blank_cnt += 1
            lab_matrix[row_idx][col_idx] = '#'
        elif lab_matrix[row_idx][col_idx] == 2:  # 비활성 바이러스
            inactivated_virus.append((row_idx, col_idx))
            lab_matrix[row_idx][col_idx] = '*'
        else:  # 벽
            lab_matrix[row_idx][col_idx] = '-'

# 예외 처리: 빈칸 수가 처음부터 0인 경우
if blank_cnt == 0:
    print(0)
    
else:  
    # 비활성 바이러스 중 M개 골라서 BFS 출발점으로 삼기
    start_indices_list = list(combinations(inactivated_virus, M))


    min_ans = float('inf')
    for start_indices in start_indices_list:
        cur_min_time = bfs(start_indices, blank_cnt)

        if cur_min_time:
            min_ans = min(cur_min_time, min_ans)
        
    if min_ans == float('inf'):  # 갱신 안된 경우
        print(-1)
    else:
        print(min_ans)

```

### [ 개선할 점 ]
1. 가지치기 : 이미 찾은 최솟값보다 오래 걸리면 조기 종료!
```python
    while dq:
        now_y, now_x = dq.popleft()
        now_time = cur_matrix[now_y][now_x]

        if now_time >= min_ans:  # 현재까지 구한 최소 시간보다 더 오래 걸리면 가지치기
            return False
```

![boj 17142 result](boj_17142_result.png)
- 이 문제에서는 근소한 차이. 가지치기 없어도 정답 처리됨.