## 1. 문제 정보 (Problem)

  - **문제 이름**: 알고리즘 수업 - 피보나치 수 1
  - **출처 및 번호**: [백준 24416번]('https://www.acmicpc.net/problem/24416')
  - **난이도**: 브론즈 1
  - **문제 요약**: 재귀호출의 실행 횟수, 동적 프로그래밍의 실행 횟수 출력

---
## 2. 핵심 아이디어 (Core Logic)
- 재귀함수를 호출하지 않고, DP로 구한 피보나치 수가 코드1의 실행 횟수와 일치한다는 것을 이용한다.
- DP 함수 한 번의 호출로 두 가지 실행 횟수를 구한다. 

---
## 3. 어려웠던 점 (Difficulties)
- 문제를 그대로 구현하고, 재귀함수와 DP함수의 코드 해당 줄에서 직접 카운트를 하면 시간 초과가 발생해서, 다른 방식을 찾아야 했다.


---
## 4. 새롭게 배운 점 (What I Learned)
피보나치 수열을 구할 때,
- 재귀호출은 Top-down 방식으로 중복 연산이 많이 발생한다.
- DP는 Bottom-up 방식으로 중복 연산을 획기적으로 줄여준다.
- 메모이제이션은 재귀호출의 Top-down 방식을 유지하되, 계산 결과를 저장하여 중복 연산을 피한다.


---
## 5. 코드 개선 (Refactoring)
- 이전 코드: 두 함수를 모두 호출해서 직접 카운트
```python
n = int(input())

def recur_fib(n):
    global recur_cnt
    if n == 1 or n == 2:
        recur_cnt += 1
        return 1
    else: 
        return recur_fib(n-1) + recur_fib(n-2)
    
def dp_fib(n):
    global dp_cnt
    dp = [-1] * (n+1) 
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp_cnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 목표: 재귀호출의 실행 횟수, 동적 프로그래밍의 실행 횟수 출력
recur_cnt = 0
dp_cnt = 0

recur_fib(n)
dp_fib(n)

print(recur_cnt, dp_cnt)
```

- 개선한 코드: 재귀함수의 호출 횟수가 기하급수적으로 발생하므로, 
직접 호출하지 않고, 피보나치 수와 코드1 실행횟수가 일치한다는 점을 이용한다.
```python
n = int(input())
    
def dp_fib(n):
    global dp_cnt
    dp = [-1] * (n+1) 
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n+1):
        dp_cnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 목표: 재귀호출의 실행 횟수, 동적 프로그래밍의 실행 횟수 출력
dp_cnt = 0
recur_cnt = dp_fib(n)

print(recur_cnt, dp_cnt)
```