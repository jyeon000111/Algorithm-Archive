## 1. 문제 정보 (Problem)

  - **문제 이름**: 스택 2
  - **출처 및 번호**: [백준 28278번]('https://www.acmicpc.net/problem/28278')
  - **난이도**: 실버 4
  - **문제 요약**: (문제를 한두 줄로 요약)

---
## 2. 핵심 아이디어 (Core Logic)


---
## 3. 어려웠던 점 (Difficulties)
- 백준 채점에서 계속 시간초과 발생
- Gemini에 물어보니, input() 입력에서 비효율이 발생할 수 있다고 함.
- sys 모듈의 `sys.stdin.readline()`로 input()을 대체할 수 있음. -> 시간 면에서 효율적 
    - 정답 처리!
    

---
## 4. 새롭게 배운 점 (What I Learned)
```python
import sys
input_data = sys.stdin.readline() 
```
- input()을 대체할 수 있다. 시간 면에서 효율적. 백준에서 시간 초과 나면 해보기.
- 입력을 여러 번 받는 경우 유리함!

---
## 5. 코드 개선 (Refactoring)

