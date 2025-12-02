## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 10807번]('https://www.acmicpc.net/problem/10807')
  - **난이도**: 브론즈 5

---
## 4. 새롭게 배운 점 (What I Learned)
- 리스트의 `.count()` 메서드
  - `리스트.count(찾을 값)`

- 메서드를 잘 활용하면 코드가 훨씬 간결해진다.
- 파이썬이 제공하는 편리한 도구(내장함수 등)를 잘 익혀두자.

---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
n = int(input())

data = list(map(int, input().split()))

v = int(input())

count_num = 0

for num in data:
    if num == v:
        count_num += 1

print(count_num)
```

- 개선한 코드 : 리스트의 `.count()` 메서드 활용
```python
n = int(input())

data = list(map(int, input().split()))

v = int(input())

print(data.count(v))
```