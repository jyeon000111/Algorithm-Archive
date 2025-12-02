## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 11718번]('https://www.acmicpc.net/problem/11718')
  - **난이도**: 브론즈 3
---
## 2. 핵심 아이디어 (Core Logic)
- EOF 처리

---
## 3. 어려웠던 점 (Difficulties)
- 입력이 끝났을 때, 프로그램을 종료하는 방법을 몰랐다. 
  -> EOF 처리를 새로 배웠다.


- try-except 구문 활용해서 EOFError가 발생하면 무한 루프를 멈추도록 했다. -> vscode에서 실행했을 때는 계속 입력을 받고 끝나지 않았다.
  - 찾아보니 터미널, IDE 환경에서는 계속 입력을 기다리는 것이 정상이라고 한다. 백준 같은 채점 사이트에서는 EOF 처리가 제대로 작동한다! 
  - 코드 실행 시 EOF 신호 주는 법
    - `Ctrl + z` 누른 후 `Enter` (Windows 환경)


---
## 4. 새롭게 배운 점 (What I Learned)
- EOF 처리 1: try-except 활용
  ```python 
  while True:
    try:
      실행할 코드
    except EOFError:
      break
  ```

- EOF 처리 2: sys.stdin 활용
  ```python
  import sys  # sys 모듈을 호출한다. 
  # sys.stdin은 파일처럼 취급할 수 있다. 
  # for 반복문으로 한 줄씩 읽으면 EOF에서 자동으로 멈춘다.
  for line in sys.stdin:
    print(line, end='')
  ```
    - 주의사항: sys.stdin으로 읽은 line에는 줄바꿈 문자(`\n`)이 이미 포함되어 있음! 
  


---
## 5. 코드 개선 (Refactoring)
- 이전 코드 (오답)
```python
while True:
    input_string = input()
    if input_string == '':
        break
    print(input_string)
```

- 입력의 끝까지 모두 읽어라 -> EOF 처리
```python
while True:
    try:
        input_string = input()
        print(input_string)
    except EOFError:
        break
```
