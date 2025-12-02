## 1. 문제 정보 (Problem)

  - **제목**: 하노이 탑 이동 순서 
  - **출처 및 번호**: [백준 11729번]('https://www.acmicpc.net/problem/11729')
  - **난이도**: 골드 5
---
## 2. 핵심 아이디어 (Core Logic)
- 재귀호출 함수
  - N 개의 원판을 3번으로 옮기는 과정은
  1. N-1 개의 원판을 2번으로 옮기고, 
  2. 가장 큰 원판을 3번으로 옮긴 다음,
  3. 다시 N-1개의 원판을 2번에서 3번으로 옮기는 과정 과 같다.

  - 원판이 1개일 때만 실제로 이동 가능
    - 이 때를 종료 조건으로 잡고, 이동 순서를 저장하고 카운트 변수를 증가시킨다.


---
## 5. 코드 개선 (Refactoring)
- for 반복문으로 보조 장대 구하는 부분 
```python
    for pole in range(1, 4):
        if pole != start_pole and pole != target_pole:
            empty_pole = pole  # 여유 공간으로 활용할 빈 장대
```
- 1, 2, 3 세 가지 장대 뿐이므로, 6에서 start_pole, target_pole 빼면 쉽게 구할 수 있다!
```python
    empty_pole = 6 - start_pole - target_pole
```
- 수학적 접근을 활용하면, 코드를 간결하고 효율적으로 개선할 수 있다.
