## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 4779번]('https://www.acmicpc.net/problem/4779')
  - **난이도**: 실버 3
---
## 2. 핵심 아이디어 (Core Logic)
  - 문제에서는 '-' * (3 ** N) 문자열에서 시작해서 3등분 하고 가운데를 공백으로 바꾸는 방식으로 순서를 설명했다.
  - 예시를 보니 작은 구조가 반복되는 게 눈에 띄었다
  - 재귀함수로 접근했다.
  - N = 0일 때, 출력되는 문자열은 '-' 이고,
  - N >= 1부터는 N-1 일 때의 문자열을 2개 붙이는데, 사이에는 N-1일 때의 문자열의 길이만큼 공백이 들어간다.


---
## 3. 어려웠던 점 (Difficulties)
- "각 줄에 N이 주어진다. 파일의 끝에서 입력을 멈춘다." 라는 입력 조건을 어떻게 처리해야 할지 몰랐다.



---
## 4. 새롭게 배운 점 (What I Learned)
- 파일 끝(EOF)에서 입력을 멈추는 방법
  1. try-except 구문 사용
    ```python
    while True:
      try:
        n = int(input())
        # n을 이용한 로직 작성

      except EOFError:
        # 더 이상 읽을 라인이 없으면(파일 끝이면) 에러가 발생하고,
        # 루프를 탈출함
        break
    ```


---
## 5. 코드 개선 (Refactoring)
- 이전 코드 : 똑같은 함수를 3번이나 호출하고 있다.
```python
return cantor_set(num - 1) + ' ' * len(cantor_set(num - 1)) + cantor_set(num - 1)
```

- 함수 중복 호출 줄이기! -> 컴퓨터의 계산량을 줄여 최적화하자.
- 한 번만 호출해서 변수에 넣고 재사용하기!

- 개선한 코드
```python
mini_cantor = cantor_set(num - 1)
return mini_cantor + ' ' * len(mini_cantor) + mini_cantor
```
