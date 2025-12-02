## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 2675번]('https://www.acmicpc.net/problem/2675')


---
## 5. 코드 개선 (Refactoring)
- 기존 코드
```python
T = int(input())

for testcase in range(T):
    # 문자열 s의 각 문자를 r번 반복해 새 문자열 p를 만든다.
    r_str, s = input().split()
    r = int(r_str)
    # p를 빈 문자열로 초기화한다.
    p = ''
    # s의 각 글자를 탐색하며, r번 곱해서 p에 더한다.
    for char in s:
        p += char * r

    print(p)
```
  - 많은 양의 문자열을 합칠 때, 비효율 발생(새로운 문자열이 메모리에 생성, 복사되는 과정 반복되기 때문에)
  - 가변 객체인 리스트에 문자열 조각을 담아뒀다가 마지막에 join으로 합치는 게 훨씬 빠르다.

- 수정한 코드
```python
# 문자열 조각들을 담을 빈 리스트를 만든다.
    p_list = []
    # s의 각 문자를 순회하며 r을 곱해 p_list에 담는다.
    for char in s:
        p_list.append(char * r)
    
    # join 메서드로 리스트의 조각들을 공백 없이 합친다.
    p = ''.join(p_list)
    print(p)
```
