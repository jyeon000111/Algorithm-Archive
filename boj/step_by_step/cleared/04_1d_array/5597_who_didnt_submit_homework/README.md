## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 5597번]('https://www.acmicpc.net/problem/5597')
  - **난이도**: 브론즈 3

---
## 4. 새롭게 배운 점 (What I Learned)
- `.remove()` 메서드를 반복 사용하는 건 비효율적이고 비싼 작업이다. 리스트 안의 데이터가 많을수록 엄청나게 느려진다.
  - 리스트에서 어떤 요소를 제거하면, 그 뒤 모든 요소들을 한 칸씩 당겨야 하기 때문.

- 체크 리스트(불리언 리스트) : 메모리를 적게 쓰고, 속도도 빠른, 효율적인 방식

---
## 5. 코드 개선 (Refactoring)
- 기존 코드
```python
# 총 학생 수는 30명. 1~30번까지 번호가 들어있는 리스트를 만든다.
student_list = list(range(1, 31))

# 28줄로 출석번호가 한줄씩 주어진다. 중복 없다.
for _ in range(28):
    # 제출한 학생의 번호를 리스트에서 제거한다.
    num = int(input())
    student_list.remove(num)

print(student_list[0])
print(student_list[1])
```


- 다른 방법 : 불리언 리스트 활용. 학생 번호를 인덱스로.
```python
# Boolean 리스트를 활용한다. 
# 인덱스를 학생 번호로 사용할 것이므로, 0번 인덱스를 사용하지 않는 31칸짜리 리스트를 만든다.
student_checked_list = [False] * 31

# 28줄로 출석번호가 한줄씩 주어진다. 중복 없다.
for _ in range(28):
    num = int(input())
    # 제출한 학생 번호에 해당하는 인덱스의 값을 True로 바꾼다.
    student_checked_list[num] = True

# 1번부터 30번까지 탐색하면서 False인 인덱스를 출력한다.
for idx in range(1, 31):
    if not student_checked_list[idx]:
        print(idx)
```
