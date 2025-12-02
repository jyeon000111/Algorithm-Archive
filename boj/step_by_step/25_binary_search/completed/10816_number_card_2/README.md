## 1. 문제 정보 (Problem)

  - **문제 이름**: 숫자 카드 2
  - **출처 및 번호**: [백준 10816번]('https://www.acmicpc.net/problem/10816')
  - **난이도**: 실버 4
  - **문제 요약**: 상근이가 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적힌 숫자 카드를 몇 개 보유하고 있는지 출력

---
## 2. 핵심 아이디어 (Core Logic)
lower bound(숫자의 시작 위치) 와 upper bound(숫자의 끝 바로 다음 위치)를 찾아서 차를 구해준다.

---
## 3. 어려웠던 점 (Difficulties)


---
## 4. 새롭게 배운 점 (What I Learned)

### 1. Lower Bound
특정 k값의 시작 위치를 찾는 알고리즘

### 2. Upper Bound
특정 k보다 처음으로 큰 값의 위치를 찾는 알고리즘

### 3. bisect 모듈로 lower bound, upper bound 쉽게 구하기
```python
from bisect import bisect_left, bisect_right

lower = bisect_left(배열, 찾는 값)  # 숫자의 시작 위치 
upper = bisect_right(배열, 찾는 값)  # 숫자의 끝 바로 다음 위치
```



---
## 5. 코드 개선 (Refactoring)
