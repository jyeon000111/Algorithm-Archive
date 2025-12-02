## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 25206번]('https://www.acmicpc.net/problem/25206')
  - **난이도**: 실버 5
---
## 2. 핵심 아이디어 (Core Logic)
- 등급을 키, 과목평점을 밸류로 하는 딕셔너리를 생성한다.
  - 등급에 해당하는 과목평점에 접근하기에 가장 효율적인 자료구조

---
## 3. 어려웠던 점 (Difficulties)
- 등급 P인 항목을 제외할 때, 방법이 여러 가지가 있어 고민되었다.
  - 문제의 의도에 맞는 가장 명시적인 방법을 선택했다.

---
## 4. 새롭게 배운 점 (What I Learned)
- EAFP와 LBYL 방식 비교
  - LBYL(조건 확인): if-else 구문
    - Look Before You Leap. 돌다리도 두드려보고 건너라.

  - EAFP(예외 처리): try-except 구문
    - Easier to Ask for Forgiveness than Permission. 허락보다 용서 구하기가 쉽다.
    - 일단 시도하고, 안되면 예외 처리


---
## 5. 코드 개선 (Refactoring)
- 처음 아이디어 (.get() 메서드 활용)
  - None 값 반환되면, continue
```python
    # 중요한 조건: 등급이 P인 항목은 계산에서 제외한다.
    # .get() 메서드로 등급 키를 찾았을 때, 딕셔너리에 없으면 다음 탐색으로 넘어간다.
    if grade_point_dict.get(grade) is None:
        continue
    else:       
        # 현재 과목의 과목평점을 구한다.
        grade_point = grade_point_dict.get(grade)
        # total_grade_point, total_credit 에 필요한 값을 더해준다.
        total_grade_point += credit * grade_point
        total_credit += credit
```

- 다른 아이디어 (try-except 구문 활용)
  - KeyError 발생 시 continue
```python
    try:
        grade_point = grade_point_dict[grade]
        total_grade_point += credit * grade_point
        total_credit += credit
    except KeyError:
        continue
```

- 최종 아이디어 (grade가 'P'일 때 continue)
  - 가장 명시적이고 직관적이다. "P를 제외한다"는 의도를 알기 쉽다.
```python
    # 중요한 조건: 등급이 P인 항목은 계산에서 제외한다.
    if grade == 'P':
        continue

    # 현재 과목의 과목평점을 구한다.
    grade_point = grade_point_dict[grade]
    # total_grade_point, total_credit 에 필요한 값을 더해준다.
    total_grade_point += credit * grade_point
    total_credit += credit
```