## 1. 문제 정보 (Problem)

  - **문제 이름**: 도키도키 간식드리미
  - **출처 및 번호**: [백준 12789번]('https://www.acmicpc.net/problem/12789')
  - **난이도**: 실버 3
  - **문제 요약**: (문제를 한두 줄로 요약)

---
## 2. 핵심 아이디어 (Core Logic)


---
## 3. 어려웠던 점 (Difficulties)
- 변수 하나를 잘못 관리해서

---
## 4. 새롭게 배운 점 (What I Learned)


---
## 5. 코드 개선 (Refactoring)
- 이전 코드: 치명적인 반례
5
2 1 3 4 5

2 -> stack 에 들어감
1 -> 바로 처리됨
3 -> 2를 stack 에서 pop() 한 후에 3도 처리해야 하는데, 바로 다음 반복인 4로 넘어감

```python
N = int(input())  # 학생의 수
order_list = list(map(int, input().split()))
# 앞에 서있는 모든 학생들의 번호표가 앞에서 뒤 순서로 주어짐 (1~N)
# 순서가 아닌 사람을 스택에 쌓았다가,
# 다시 순서대로 들어갈 수 있는 라인으로 보냈을 때 모두 통과하면, 간식 받을 수 있음

# 목표: 간식을 받을 수 있으면 'Nice', 그렇지 않다면 'Sad' 출력
get_snack = True  # 간식을 받을 수 있다고 가정

current_snack_num = 1  # 이번에 간식 받을 사람 번호
stack = []  # 자기 순서 아닌 사람 담는 스택

for num in order_list:  # 번호표 하나씩 체크
    if num == current_snack_num:  # 간식 받을 순서 맞으면 통과
        current_snack_num += 1
    else:  # 간식 받을 순서 아닌 경우
        # 스택에 내림차순으로 쌓여야 한다.
        # 스택이 비었으면 push
        if not stack:
            stack.append(num)
        # 스택에 값이 있을 때
        else:
            # 스택의 마지막 값보다 현재 번호표가 작을 때만 push
            if stack[-1] > num:
                stack.append(num)
            # 스택의 마지막 값이 더 작으면, current_snack_num 인지 체크
            else:
                if stack[-1] == current_snack_num:
                    stack.pop()  # 맞으면 해당 번호 제거하고 현재 간식 번호 1 증가
                    current_snack_num += 1
                else:  # -> 아니면 간식 못 받음.. 반복 종료!
                    get_snack = False
                    break  # for num 종료

if get_snack:
    print('Nice')
else:
    print('Sad')
```