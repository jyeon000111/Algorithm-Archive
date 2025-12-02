## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 0000번]('URL주소')
  - **난이도**: 
  - **문제 요약**: (문제를 한두 줄로 요약)

---
## 2. 핵심 아이디어 (Core Logic)


---
## 3. 어려웠던 점 (Difficulties)
- 2가지 패턴이 가능한데, 각각 어떻게 비교해야 할지 모르겠다.
  - 체스판 규칙에 따라 색칠되었는지, 어느 부분을 다시 칠해야 하는지 개수를 반환하는 함수를 만든다?? (2가지 패턴을 모두 체크하고, 둘 중 작은 값을 반환)

---
## 4. 새롭게 배운 점 (What I Learned)


---
## 5. 코드 개선 (Refactoring)
- 이전 함수 코드
```python
def count_to_change_for_chess(square):
    '''8글자의 문자열 8개로 이루어진 리스트를 인자로 받아
    8행, 8열이 체스패턴에 맞게 칠해졌는지 확인하고,
    다시 칠해야 하는 개수를 반환하는 함수입니다.
    단, 체스패턴이 2가지가 가능하므로 
    각각 구해서 더 작은 값을 반환합니다.
    '''
    
    pattern1_count = 0  # W로 시작하는 패턴
    # (홀수, 홀수) = W, (짝수, 짝수) = W, (홀수, 짝수) = B, (짝수, 홀수) = B
    # 인덱스의 합이 짝수면, W, 홀수면 B여야 한다.
    # 규칙과 다르면 count +1 추가
    for row_idx, line in enumerate(square):
        for col_idx, char in enumerate(line):
            if (row_idx + col_idx) % 2 == 0:
                if char != 'W':
                    pattern1_count += 1
            else:
                if char != 'B':
                    pattern1_count += 1  

    pattern2_count = 0  # B로 시작하는 패턴
    for row_idx, line in enumerate(square):
        for col_idx, char in enumerate(line):
            if (row_idx + col_idx) % 2 == 0:
                if char != 'B':
                    pattern2_count += 1
            else:
                if char != 'W':
                    pattern2_count += 1

    return min(pattern1_count, pattern2_count)
```

- 2가지 패턴을 따로 for문으로 돌리지 않고, 한번에 같이 카운트할 수 있다.

- 개선한 함수 코드
```python
    pattern2_count = 0  # B로 시작하는 패턴은 위와 반대의 경우에 카운트

    for row_idx, line in enumerate(square):
        for col_idx, char in enumerate(line):
            if (row_idx + col_idx) % 2 == 0:
                if char != 'W':
                    pattern1_count += 1
                else:
                    pattern2_count += 1
            else:
                if char != 'B':
                    pattern1_count += 1  
                else:
                    pattern2_count += 1

    return min(pattern1_count, pattern2_count)
```