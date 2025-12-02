## 1. 문제 정보 (Problem)

  - **문제 이름**: 카드2
  - **출처 및 번호**: [백준 2164번]('https://www.acmicpc.net/problem/2164')
  - **난이도**: 실버 4
  - **문제 요약**: N장의 카드가 1번(위)부터 N번(아래)까지 순서대로 쌓여있다. 맨 위 카드를 버리고, 그다음 맨 위 카드를 맨 아래로 옮기는 동작을 반복하여 마지막에 남는 카드를 찾는 문제.

---
## 2. 핵심 아이디어 (Core Logic)
- collections 모듈의 deque 자료구조 활용! 
  - 리스트의 O(N) 시간 복잡도를 가진 연산을 O(1)로 해결하기 위해

---
## 3. 어려웠던 점 (Difficulties)
- insert 연산 때문에 계속 시간 초과가 발생




---
## 4. 새롭게 배운 점 (What I Learned)
- insert 연산이 오래 걸리는 이유?
    - 리스트는 배열처럼 연속된 메모리 공간에 데이터를 저장함.
    - 맨 앞에 데이터를 추가하려면 기존 모든 데이터를 한 칸씩 뒤로 밀어야 함.
    - 리스트의 요소가 N개일 때, 시간 복잡도 O(N)

- 반대로 pop(0) 활용한다면? 마찬가지
  - 맨 앞 데이터를 제거하면, 기존 모든 데이터를 한 칸씩 앞으로 땡겨야 함.
  - 시간 복잡도 O(N) 

- collections 모듈의 deque(덱, double-ended queue)
  - 양쪽 끝에서 데이터를 추가, 제거하는 데 특화된 효율적인 자료구조
  - 모든 데이터 밀어낼 필요 없이 시간 복잡도 O(1) 안에 작업을 끝낼 수 있음
```python
from collections import deque

queue = deque(range(1, N+1))  # 덱 자료구조에 데이터 담기

queue.popleft()  # 맨 왼쪽 원소 제거
queue.appendleft(x)  # 맨 왼쪽에 x 추가

```

`dq = deque()  # 비어있는 덱 초기화`

---
## 5. 코드 개선 (Refactoring)
- 1차 시도 : 백준 채점 시간 초과
```python
N = int(input())  # 1~N 번호 카드 (1번이 제일 위)

stack = [num for num in range(N, 0, -1)]  # 제일 위 카드가 오른쪽 끝
while len(stack) > 1:
    stack.pop()
    stack.insert(0, stack.pop())

print(*stack)
```

- 2차 시도 : 백준 채점 시간 초과
```python
N = int(input())  # 1~N 번호 카드 (1번이 제일 위)

stack = [num for num in range(N, 0, -1)]  # 제일 위 카드가 오른쪽 끝
top = N-1
while top > 1:
    top -= 1  # 맨 위 카드 버리기
    # 맨 위 카드를 맨 아래 카드 밑으로 옮기기
    stack.insert(0, stack[top])

print(stack[0])
```
- 최종 코드 : deque 자료구조 활용
```python
from collections import deque

N = int(input())  # 1~N 번호 카드 (1번이 제일 위)

queue = deque(range(N, 0, -1))  # 제일 위 카드가 오른쪽 끝

while len(queue) > 1:
    # 제일 위 카드를 버린다.
    queue.pop()
    # 제일 위 카드를 제일 아래(왼쪽 끝)로 옮긴다.
    queue.appendleft(queue.pop())

print(queue[0])
```