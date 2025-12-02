## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 2941번]('https://www.acmicpc.net/problem/2941')
  - **난이도**: 실버 5
---
## 2. 핵심 아이디어 (Core Logic)
- 크로아티아 알파벳을 한 글자로 치환한 후, 길이를 구한다.

---
## 3. 어려웠던 점 (Difficulties)
- .replace() 메서드를 쓰고, 재할당을 하지 않아서 무한루프에 빠졌다.


---
## 4. 새롭게 배운 점 (What I Learned)
- 문자열에서 특정 문자열을 찾아서 제거하는 법
  - .replace() 메서드로 제거할 문자열을 빈 문자열로 바꿔준다.
  `문자열.replace(제거할 문자열, '', [, 제거할 개수])`
  - 제거할 개수를 입력하지 않으면, 모두 제거된다.
  - 주의할 점: 문자열은 불변 객체! 기존 문자열을 바꿔주는 것이 아니라 새로운 문자열을 반환해줌 -> 변수에 다시 할당해주어야 함.

- 문자열에서도 멤버십 연산자 in을 쓸 수 있다.

---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
# 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는가
word = input()

# 크로아티아 알파벳 리스트를 만든다.
cro_alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳을 하나하나 찾아 제거하면서, 개수를 센다.
cro_alpha_count = 0
for cro_alpha in cro_alpha_list:
    while cro_alpha in word:
        word = word.replace(cro_alpha, '', 1)
        cro_alpha_count += 1

# 남은 문자열의 개수를 구한다.
remaining_chars_count = len(word)

# 두 종류의 개수를 더하여 출력 
print(cro_alpha_count + remaining_chars_count)
```

- while 문과 카운터 변수가 불필요하게 쓰여서 비효율적

- 목적은 단순히 개수를 세는 것. 크로아티아 알파벳을 제거하기 보다 한 글자로 변경해주면, len함수로 한 번에 글자 수를 도출할 수 있다.


- 개선한 코드
```python
# 주어진 단어에서 크로아티아 알파벳을 찾아 한 글자로 바꿔준다.
for cro_alpha in cro_alpha_list:
    word = word.replace(cro_alpha, '*')

# 변경된 문자열의 길이를 출력한다.
print(len(word))
```

