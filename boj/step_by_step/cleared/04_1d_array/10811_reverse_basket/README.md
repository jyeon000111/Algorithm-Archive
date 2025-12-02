## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 10811번]('https://www.acmicpc.net/problem/10811')
  - **난이도**: 브론즈 2

---
## 4. 새롭게 배운 점 (What I Learned)
- 슬라이스 할당 Slice Assignment
  - `리스트[인덱스1:인덱스2] = 교체할 리스트`
  - 교체할 리스트가 슬라이싱된 길이보다 길어도 상관없다!

- 슬라이싱 문법을 활용해 역순으로 뒤집기
  - `리스트[::-1]`

- 슬라이싱 연달아 적용 가능 (슬라이싱의 결과물도 리스트이기 때문)

---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
for case in range(m):
    # 왼쪽에서 i번째 ~ j번째 바구니 순서를 역순으로 바꾼다. (인덱스로 치면 i-1, j-1)
    # 슬라이싱해서 3조각으로 나눈 뒤, 중간 조각만 역순으로 뒤집어서 다시 합친다.
    i, j = map(int, input().split())
    basket_part1 = basket[:i-1]
    basket_part2 = basket[i-1:j]
    basket_part3 = basket[j:]
    
    basket_part2.reverse()
    basket = basket_part1 + basket_part2 + basket_part3
  ```

  - 슬라이스 할당
```python
for case in range(m):
    # 왼쪽에서 i번째 ~ j번째 바구니 순서를 역순으로 바꾼다. (인덱스로 치면 i-1, j-1)
    # 해당 부분을 역순으로 뒤집어서 슬라이스 할당한다.
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1]
```