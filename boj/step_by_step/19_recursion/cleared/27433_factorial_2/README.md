# The "Why" and "How"

## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 27433번]('https://www.acmicpc.net/problem/27433')
  - **난이도**: 브론즈 5
---
## 2. 핵심 아이디어 (Core Logic)
- 재귀함수 활용



---
## 3. 어려웠던 점 (Difficulties)

- 제출하니 런타임 에러
  - 0을 입력 받았을 때를 처리해줘야 함.
  - 문제에서 주어진 입력 조건: '첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.'


---
## 4. 새롭게 배운 점 (What I Learned)
- 입력 조건을 꼼꼼히 확인하고, 예외적인 경우를 어떻게 처리할지 고려해서 코드를 짜야겠다.



---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
def factorial(num):
    """정수를 입력받아
    팩토리얼 값을 반환하는 함수입니다.
    """
    if num == 1:
        return 1
    return num * factorial(num - 1)
```

- 입력 값으로 0이 들어왔을 때? 0! = 1

```python
def factorial(num):
    """정수를 입력받아
    팩토리얼 값을 반환하는 함수입니다.
    """
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)
```