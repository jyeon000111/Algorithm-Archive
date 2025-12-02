## 1. 문제 정보 (Problem)

  - **문제 이름**: 신나는 함수 실행
  - **출처 및 번호**: [백준 9184번]('https://www.acmicpc.net/problem/9184')
  - **난이도**: 실버 2
  - **문제 요약**: 주어진 재귀 함수 w(a, b, c)의 결과를 메모이제이션(Memoization) 기법을 이용해 효율적으로 계산하기 

---
## 2. 핵심 아이디어 (Core Logic)
- DP의 메모이제이션 기법을 활용해, 한 번 계산한 결과를 3차원 배열에 저장해놓고 다시 쓴다.

---
## 3. 어려웠던 점 (Difficulties)
- a, b, c 세 개의 변수에 대한 계산 결과를 어떻게 저장해야 할지 어려웠다.
- 3차원 리스트에 저장하는 경우, 초기값을 어떻게 설정해야 할지 고민됐다.
  - 절대 나올 수 없는 값이어야 기록 여부를 확인할 수 있다.
  - 기록 여부를 별도의 boolean 배열에 기록하는 방법도 있다.


---
## 4. 새롭게 배운 점 (What I Learned)
- a, b, c 세 개의 변수에 대한 계산 결과 저장하는 방법
  1. 3차원 리스트
    ```python
    memo = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    ```
    - 장점: 속도가 가장 빠름(인덱싱)
    - 단점: 메모리 공간 낭비 가능성(안 쓰는 공간 할당)
    - 모든 경우를 다 채워야 할 때 적합
  2. 딕셔너리 + 튜플 키
    - 장점: 메모리 효율적
    - 단점: 리스트보다 약간의 오버헤드 존재
    - 계산되지 않는 경우가 많을 때 적합
  3. `@cache` 데코레이터
    - 메모이제이션을 자동으로 해줌. 함수 위에 한 줄 붙여주면 파이썬이 알아서 값을 확인하고 저장해줌.
    ```python
    from functools import cache

    @cache
    def w(a, b, c):
        pass
    ```
    - 장점: 코드가 극도로 간결하고 직관적
    - 코딩테스트, 실무 등 실전 코딩 상황에 적합



---
## 5. 최종 코드 
```python
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def recur(a, b, c):
    '''
    1. a, b, c 중 0 이하인 수가 있다면 1 반환
    2. a, b, c 중 20 초과인 수가 있다면 w(20, 20, 20) 반환
    3. a < b < c 면, w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) 반환
    4. 그 외에는 w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) 반환
    '''
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)   
     
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
    else:
        dp[a][b][c] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)

    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {recur(a, b, c)}')
```
