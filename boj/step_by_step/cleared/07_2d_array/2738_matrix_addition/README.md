## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 2738번]('https://www.acmicpc.net/problem/2738')
  - **난이도**: 브론즈 3
  - **문제 요약**: N*M 크기의 두 행렬 A와 B를 입력받아, 두 행렬을 더한 결과를 출력한다.
---
## 2. 핵심 아이디어 (Core Logic)
- 모든 행과 열의 인덱스를 순회하며, 각 요소를 더해준다.(중첩 for문)

---
## 3. 어려웠던 점 (Difficulties)
- 0으로 초기 설정된 n행 m열의 2차원 행렬 만들기
```python
a_plus_b = [[0] * m] * n  
# 얕은 복사 
# -> [0, 0, 0] 리스트 하나 생성 후, 주소만 n번 복사하는 것과 같음. 
# -> 모든 행이 똑같은 하나의 리스트를 가리키게 됨.
```

  - 2차원 리스트는 리스트 컴프리헨션으로 만드는 것이 정석
```python
a_plus_b = [[0]*m for _ in range(n)]
```

---
## 4. 새롭게 배운 점 (What I Learned)
- 변경 가능한(mutable) 객체를 곱셈(*)으로 복제하면 얕은 복사 문제가 발생.
- [0]*m 에서 0은 변경 불가능한(immutable) 객체이기 때문에 안전하다.
- 곱셈(*)으로 리스트를 만들 땐, 안에 담긴 요소가 변경 불가능한지 항상 생각해봐야 한다.

---
## 5. 코드 개선 (Refactoring)
- 기존 코드 (정석적인 방법)
```python
n, m = map(int, input().split())
a = []
b = []
for row in range(n):
    a.append(list(map(int, input().split())))
for row in range(n):
    b.append(list(map(int, input().split())))

# 둘을 더한 n행 m열의 2차원 행렬을 0으로 초기화한다.
a_plus_b = [[0]*m for _ in range(n)]
for row_idx in range(n):
    for col_idx in range(m):
        a_plus_b[row_idx][col_idx] = a[row_idx][col_idx] + b[row_idx][col_idx]

for row in a_plus_b:
    print(*row)
```

- 다른 방법 (zip 함수 활용)
```python
for row_a, row_b in zip(a,b):
    result_row = [x + y for x, y in zip(row_a, row_b)]
    print(*result_row)
```