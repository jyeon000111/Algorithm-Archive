## 1. 문제 정보 (Problem)

  - **문제 이름**: N과 M (2)
  - **출처 및 번호**: [백준 15650번]('https://www.acmicpc.net/problem/15650')
  - **난이도**: 실버 3
  - **문제 요약**: 1~N 자연수 중 중복 없이 M개를 고른 수열 (오름차순) 구하기

---
## 2. 핵심 아이디어 (Core Logic)
- 오름차순 정렬된 수열 -> 탐색의 시작점을 인자로 하는 재귀함수

---
## 4. 새롭게 배운 점 (What I Learned)
- 오름차순 정렬된 수열을 뽑을 때는 탐색의 시작점을 인자로 받으면 효율적인 탐색이 가능하다. 다음 숫자부터 탐색하도록 하면 중복 체크를 할 필요가 없어 visited 배열도 필요 없다.

---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
def print_sub(cnt):
    if cnt == M:
        print(*result)
        return
    
    for num in range(1, N+1):  # 1~N 까지 숫자를 하나씩 꺼내기
        # 방문한 적 없으면
        if not visited[num]:
        # 결과리스트 비었거나 마지막 수보다 크면
        # -  결과에 추가 후 방문 표시 -> 다음 재귀
            if not result or num > result[-1]:
                result.append(num)
                visited[num] = True

                print_sub(cnt + 1)

                # 다녀와서 방문 흔적 지우기. 마지막 값 pop
                result.pop()
                visited[num] = False

        # 방문한 적 있으면 패스
```
- 오름차순 규칙 때문에 visited 배열과 `if not result or num > result[-1]:`의 두 가지 장치 사용 -> 비효율적

- 탐색 시작점(start)을 인자로 넘겨 받는 방식으로, 다음 숫자부터 탐색하기
  - visited 배열, `if num > result[-1]:` 조건문 불필요
  - 빠르고 간결함!

- 개선한 코드
```python
result = []  # 수열을 담을 리스트

def print_sub(start): 
    '''탐색 시작점을 인자로 받아, 
    길이 M의 수열을 출력하는 함수입니다.
    오름차순으로 수를 중복없이 선택합니다.
    '''
    if len(result) == M:
        print(*result)
        return
    
    for num in range(start, N+1):  # 시작점부터 N 까지 숫자를 하나씩 꺼내기
        result.append(num)  # 첫번째 숫자를 결과 리스트에 담는다.
        # num+1을 시작점으로 하는 탐색을 재귀호출한다.
        print_sub(num + 1)
        result.pop()


print_sub(1)
```