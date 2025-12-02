## 1. 문제 정보 (Problem)

  - **문제 이름**: 연산자 끼워넣기
  - **출처 및 번호**: [백준 14888번]('https://www.acmicpc.net/problem/14888')
  - **난이도**: 실버 1
  - **문제 요약**: 첫째 줄에 만들 수 있는 식의 결과의 최댓값, 둘째 줄에 최솟값 출력

---
## 2. 핵심 아이디어 (Core Logic)
- 백트래킹 알고리즘 : 불필요한 탐색 차단
- 숫자 사이사이에 무조건 연산자가 들어간다.
- 연산자 N-1개의 순서를 정하는 리스트를 생성
1. 숫자 리스트, 연산자 리스트를 인자로 받아 계산 결과 도출하는 함수 만들기
2. 백트래킹으로 연산자 리스트 만들기. 깊이 끝에 도달하면 계산 결과 구하기
3. 최솟값, 최댓값 갱신하며 끝까지 진행.


---
## 5. 코드 개선 (Refactoring)
- 이전 코드 : 게산 결과를 구하는 함수에 stack을 사용해서 복잡하게 만듬.
```python
def calculate(num_list, oper_list):
    '''숫자 리스트(길이 N), 연산자 리스트(길이 N-1)를 인자로 받아 
    계산 결과를 반환하는 함수입니다.
    '''
    temp = []  # 계산 과정에 필요한 스택
    for idx in range(N): # 0~N-1 인덱스 순회
        # 빈 스택일 때는 현재 인덱스의 숫자와 연산자 모두 추가
        if not temp:
            temp.append(num_list[idx])
            temp.append(oper_list[idx])
        # 스택에 값이 있을 때(숫자 하나, 연산자 하나)
        else: 
            # 스택에서 연산자, 숫자 모두 pop하고 계산 결과를 push한다.
            oper = temp.pop()
            num1 = temp.pop()
            num2 = num_list[idx]
            if oper == '+':
                temp.append(num1 + num2)
            elif oper == '-':
                temp.append(num1 - num2)
            elif oper == '*':
                temp.append(num1 * num2)
            else:  # 나눗셈 연산자일 경우
                if num1 < 0:  # 음수일 때, 양수로 바꾼 뒤 몫을 구하고 음수로 바꾼다.
                    temp.append(-(-num1 // num2))
                else:
                    temp.append(num1 // num2)
            if idx < N-1:  # 인덱스 범위 벗어나지 않으면, 연산자도 스택에 push
                temp.append(oper_list[idx])

    return temp[0]
```
- 앞에서부터 순차적으로 계산하는 방식이므로, stack이 불필요함.


- 개선한 코드 : 우선순위 무시하고 앞에서부터 계산하는 로직 그대로 구현 (for 반복문)
```python
def calculate(num_list, oper_list):
    '''숫자 리스트(길이 N), 연산자 리스트(길이 N-1)를 인자로 받아 
    계산 결과를 반환하는 함수입니다.
    '''
    num1 = num_list[0]
    for idx in range(N-1): # 0~N-2 인덱스 순회
        num2 = num_list[idx + 1]
        oper = oper_list[idx]
        if oper == '+':
            num1 += num2
        elif oper == '-':
            num1 -= num2
        elif oper == '*':
            num1 *= num2
        else:
            if num1 < 0:
                num1 = -(-num1 // num2)
            else:
                num1 //= num2

    return num1
```
