## 1. 문제 정보 (Problem)

  - **문제 이름**: 랜선 자르기
  - **출처 및 번호**: [백준 1654번]('https://www.acmicpc.net/problem/1654')
  - **난이도**: 실버 2
  - **문제 요약**: N개를 만들 수 있는 랜선의 최대 길이

---
## 2. 핵심 아이디어 (Core Logic)
- Parametric Search

---
## 3. 어려웠던 점 (Difficulties)
- 탐색 범위의 왼쪽 경계를 0으로 잘못 설정해서 계속 오답이 나왔다.
    - ZeroDivisionError 발생 확률이 높아진다.
    - 해가 될 수 있는 랜선 길이의 최솟값은 1이므로 left를 1로 설정했어야 한다.ㅠ 

---
## 4. 새롭게 배운 점 (What I Learned)


---
## 5. 코드 개선 (Refactoring)

