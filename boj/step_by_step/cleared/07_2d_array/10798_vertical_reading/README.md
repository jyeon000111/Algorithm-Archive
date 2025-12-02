## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 10798번]('https://www.acmicpc.net/problem/10798')
  - **난이도**: 브론즈 1
  - **문제 요약**: 
    - 5줄의 입력을 받아, 세로로 공백없이 읽어내려가며 출력한다.
    - 각 줄에는 1~15개의 글자들이 주어진다.


---
## 2. 핵심 아이디어 (Core Logic)
- 5*15 2차원 리스트를 ''(빈 문자열)로 초기화
- 5줄을 입력받으며, 리스트를 수정.
- 열 인덱스 -> 행 인덱스 순으로 중첩 for문 사용하여 세로로 읽기

---
## 5. 코드 개선 (Refactoring)
- 다른 방법: 
  - 입력받은 데이터 안에서, 가장 긴 줄의 길이까지만 세로로 읽기
  - 리스트 안에 문자열을 넣어도 인덱싱 연이어서 할 수 있음. (2차원 리스트와 비슷)
  - try-except 구문으로 존재하지 않는 인덱스는 건너뛰며 세로로 읽기
```python
# 5줄을 문자열 상태로 모두 리스트에 담는다.
lines = []
for _ in range(5):
    lines.append(list(input()))

# 가장 긴 줄의 길이를 구한다.
max_length = 0
for line in lines:
    if len(line) > max_length:
        max_length = len(line)

# 가장 긴 줄의 길이까지만 세로로 읽어 출력한다.
for col_idx in range(max_length):
    for row_idx in range(5):
        # 일단 해보고,
        try:
            print(lines[row_idx][col_idx], end='')
        # 해당 인덱스 없으면 continue로 넘어간다.
        except IndexError:
            continue
```
