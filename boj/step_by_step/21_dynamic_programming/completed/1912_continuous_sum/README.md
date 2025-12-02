## 1. 문제 정보 (Problem)

  - **문제 이름**: 연속합
  - **출처 및 번호**: [백준 1912번]('https://www.acmicpc.net/problem/1912')
  - **난이도**: 실버 2
  - **문제 요약**: n개의 정수로 주어진 임의의 수열. 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 최댓값 구하기

---
## 2. 핵심 아이디어 (Core Logic)
- i번째 인덱스에서 끝나는 배열의 최댓값을 dp[i] 에 저장
- dp[0] = arr[0]
- i > 0: dp[i] = max(arr[i], dp[i-1] + arr[i])  

---
## 3. 어려웠던 점 (Difficulties)


---
## 4. 새롭게 배운 점 (What I Learned)


---
## 5. 코드 개선 (Refactoring)

