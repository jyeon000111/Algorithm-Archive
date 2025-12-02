## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 10810번]('https://www.acmicpc.net/problem/10810')
  - **난이도**: 브론즈 3


## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
# 공을 M 번 넣는다
for case in range(m):
    i, j, k = map(int, input().split())
    # i번~j번 바구니까지 k번호의 공을 넣는다.
    # 바구니에 이미 있으면, 기존 공 빼고 새로 넣는다.
    # - 리스트의 인덱스로 치면 i-1 부터 j-1의 값을 k로 재할당한다.
    for index in range(i-1, j):
        basket[index] = k
```

- 다른 방법
```python
    # 슬라이스 할당.
    length = j - i + 1  # 교체할 부분의 길이
    basket[i-1:j] = [k] * length
```