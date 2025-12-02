## 1. 문제 정보 (Problem)

  - **문제 이름**: 키로거
  - **출처 및 번호**: [백준 5397번]('https://www.acmicpc.net/problem/5397')
  - **난이도**: 실버 2
  - **문제 요약**: 입력 순서대로 키 문자열이 주어졌을 때, 비밀번호 구하기

---
## 2. 핵심 아이디어 (Core Logic)
- 커서 앞과 뒤를 두 개의 덱으로 만들어 관리한다. 양끝의 추가, 삭제가 효율적인 덱의 장점을 극대화한다.

---
## 3. 어려웠던 점 (Difficulties)
- deque 자료구조를 사용한 건 좋았지만, 
  커서 위치 때문에 중간에서 데이터를 추가하고 삭제해야 해서 시간 초과가 발생했다.
  - deque은 양 끝 데이터의 추가 삭제가 효율적이므로, 커서 앞 뒤로 2개의 deque을 만들어야 한다!

---
## 4. 새롭게 배운 점 (What I Learned)
- 덱 자료구조의 중간에서 데이터를 추가, 삭제해야 한다면, 2개 이상의 덱으로 나누어 쓰는 것도 매우 효과적인 방법이다.

- `sys.stdin.readline()` 은 백준 채점에서 효율적인 방법이지만, 줄바꿈 문자 (`\n`)까지 포함한 한 줄을 읽어들인다.
    - 양쪽 끝의 공백, 줄바꿈 문자를 제거해주는 `.strip()` 메서드를 사용해서 해결 가능



---
## 5. 코드 개선 (Refactoring)
- 이전 코드: 백준 채점 결과 시간 초과
- deque 하나와 커서 변수 활용 -> 덱 중간에서 데이터를 추가, 삭제하게 되어, 덱 자료구조의 장점을 살리지 못함.
```python
from collections import deque
# 효율적인 수정을 위해 deque 자료구조 사용

T = int(input())
for _ in range(T):
    input_key = input()
    # 목표: 입력 순서대로 키 문자열이 주어졌을 때, 비밀번호 출력
    # 백스페이스(-) : 바로 앞 글자 삭제
    # 화살표(<, >) : 커서 위치 1칸 이동
    now = 0  # 커서
    # 나머지 문자는 비밀번호의 일부
    dq = deque()
    for key in input_key:  # 입력 순서대로 키 꺼내기
        if key == '-':  # 백스페이스가 입력된 경우
            if now > 0:  # 커서가 0보다 크면 커서 앞의 값 제거
                now -= 1
                dq[now] = '-'  # 지울 값 표시
                dq.remove('-')
            else:  # 커서가 0 이하면, continue
                continue
        elif key == '<':  # 왼쪽 화살표 입력된 경우
            if now > 0:  # now > 0 이면 커서 이동
                now -= 1
            else:  # now가 0 이하면 continue
                continue
        elif key == '>':  # 오른쪽 화살표 입력된 경우
            if now < len(dq):  # dq의 길이보다 작으면 커서 이동
                now += 1
            else:
                continue
        else:  # 나머지 문자는 dq에 그대로 추가
            dq.insert(now, key)
            now += 1
    print(''.join(dq))
```

- 개선한 코드: 백준 채점 결과 정답
- 커서 앞과 뒤를 두 개의 덱으로 나누어, 덱의 양 끝에서만 추가, 삭제가 이루어지도록 함. -> 덱의 장점 극대화. 효율 향상!
- `else: continue` 부분은 없어도, if문에 걸리지 않으면 자동으로 다음 반복으로 넘어감. 코드의 간결함을 위해 삭제

```python
import sys
from collections import deque
# 효율적인 수정을 위해 deque 자료구조 사용

T = int(sys.stdin.readline())
for _ in range(T):
    input_key = sys.stdin.readline().strip()
    # 목표: 입력 순서대로 키 문자열이 주어졌을 때, 비밀번호 출력
    # 백스페이스(-) : 바로 앞 글자 삭제
    # 화살표(<, >) : 커서 위치 1칸 이동
    dq1 = deque()  # 커서 앞
    dq2 = deque()  # 커서 뒤

    # 나머지 문자는 비밀번호의 일부
    for key in input_key:  # 입력 순서대로 키 꺼내기
        if key == '-':  # 백스페이스가 입력된 경우
            if dq1:  # 커서 앞에 값이 있으면
                dq1.pop()  # 제거
        elif key == '<':  # 왼쪽 화살표 입력된 경우
            if dq1:  # 커서 앞에 값이 있으면
                dq2.appendleft(dq1.pop())  # dq1 맨 뒤 값을 dq2 맨 앞으로 이동
        elif key == '>':  # 오른쪽 화살표 입력된 경우
            if dq2:  # 커서 뒤에 값이 있으면
                dq1.append(dq2.popleft())# dq2의 맨 앞 값을 dq1의 맨 뒤로 이동
        else:  # 나머지 문자는 dq1에 그대로 추가
            dq1.append(key)

    print(''.join(dq1 + dq2))
```