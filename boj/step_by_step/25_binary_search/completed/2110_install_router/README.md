## 1. 문제 정보 (Problem)

  - **문제 이름**: 공유기 설치
  - **출처 및 번호**: [백준 2110번]('https://www.acmicpc.net/problem/2110')
  - **난이도**: 골드 4
  - **문제 요약**: 

---
## 2. 핵심 아이디어 (Core Logic)
- Parametric Search로 현재 mid 값이 해가 될 수 있는지 검사한다.
- 함수로 C개 이상의 공유기를 설치할 수 있는지 체크하고 범위를 좁혀나간다.

---
## 3. 어려웠던 점 (Difficulties)
- 공유기 설치 가능 여부를 어떻게 판단해야 할지 고민되었다.

---
## 4. 새롭게 배운 점 (What I Learned)
#### 가지치기의 효율 판단
- "검사하는 비용보다 잘라내서 얻는 이득이 훨씬 큰가??"
- 값싼 비용으로 거대한 탐색 영역을 잘라낼 수 있을 때만 가지치기 !! 

1. 검사 비용이 저렴한가 ?
    - 조건문이 무거우면 안 됨. O(1) 의 단순 비교, 산술 계산일 때만 좋은 가지치기
    
2. 얼마나 많이 잘라내는가 ?
    - 성공했을 때 막대한 양의 후속 계산을 건너뛰어야만 의미 있음. (예: 백트래킹)
    



---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
def install(dist, N):
    if left_house + (C - 1) * dist > right_house:  # 가장 먼 집을 넘어서면 반환
        return False

    cnt = 1  # 맨 왼쪽에 하나 설치
    cur_i = 0  # 마지막으로 설치한 위치
    while True:
        if cnt == C:
            return True
        for next_i in range(cur_i + 1, N):
            if houses[next_i] >= houses[cur_i] + dist:
                cnt += 1  # 설치
                cur_i = next_i
                break  # for next_i
        else:
            break

    return False


N, C = map(int, input().split())  # N은 집의 개수, C는 공유기의 개수
# 집의 좌표들
houses = []

for _ in range(N):
    houses.append(int(input()))

left_house = min(houses)
right_house = max(houses)

houses.sort()

left = 1
right = right_house

while left <= right:
    mid = (left + right) // 2  # 공유기 사이의 거리

    if install(mid, N):  # 설치 가능하면 거리를 넓힌다.
        left = mid + 1
    else:  # 불가능하면 거리를 좁힌다.
        right = mid - 1

print(right)
```

- 문제점:
1. right 범위 설정 문제. 거리가 아닌 좌표를 넣음. -> 첫번째 집과 마지막 집 사이의 거리로 바꾸기
    - 만약 첫번째 집이 9억, 마지막 집이 10억이면, 1~1억만 조사하면 됨.
    - 내 첫번째 풀이에서는 10억을 그대로 넣어서 1~10억을 조사하게 되는 치명적인 비효율 발생
2. install 함수의 복잡함. -> 간결하게 바꾸기

- 최종 코드
```python
def install(dist, N):
    '''
    공유기 사이의 간격과 집의 개수를 인자로 받아,
    C개의 공유기를 모두 설치할 수 있는지 확인하고,
    가능하면 True, 불가능하면 False를 반환한다.
    '''
    cnt = 1  # 맨 왼쪽에 하나 설치
    cur_i = 0  # 마지막으로 설치한 위치

    for next_i in range(1, N):
        if houses[next_i] >= houses[cur_i] + dist:
            cnt += 1
            cur_i = next_i

    return cnt >= C


# 목표: C개의 공유기를 N개의 집에 설치할 때, 가장 인접한 두 공유기 사이의 최대 거리 구하기
# => 파라메트릭 서치
N, C = map(int, input().split())  # N은 집의 개수, C는 공유기의 개수
# 집의 좌표들
houses = []

for _ in range(N):
    houses.append(int(input()))

left_house = min(houses)
right_house = max(houses)

houses.sort()

left = 1
right = right_house - left_house

while left <= right:
    mid = (left + right) // 2  # 공유기 사이의 거리

    if install(mid, N):  # 설치 가능하면 거리를 넓힌다.
        left = mid + 1
    else:  # 불가능하면 거리를 좁힌다.
        right = mid - 1

print(right)

```