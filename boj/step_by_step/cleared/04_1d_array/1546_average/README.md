## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 1546번]('https://www.acmicpc.net/problem/1546')
  - **난이도**: 브론즈 1
---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
# 점수 중 최댓값을 m이라고 한다.
m = max(score_list)

# 모든 점수를 점수/m*100으로 고친다.
new_score_list = list(map(lambda x: x/m*100, score_list))

# 새로운 평균을 구한다.
print(sum(new_score_list) / len(new_score_list))
```

- 시험 본 과목 수를 변수 n으로 입력받아놓고, 사용하지 않았다. len(new_score_list) 대신 들어가면 됨.

- 수학적 접근으로 코드 간소화

```python
# 모든 점수를 점수/m*100으로 고친 후, 새로운 평균을 출력한다.
# 수학적으로 새로운 평균은 현재 평균/m*100과 같다.
# (a/m*100 + b/m*100 + c/m*100) / 3 == (a + b + c) / m*100 / 3
print(sum(score_list) / (m*100) / n)
```