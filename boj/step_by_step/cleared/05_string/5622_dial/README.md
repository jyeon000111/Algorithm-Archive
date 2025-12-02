## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 5622번]('https://www.acmicpc.net/problem/5622')
  - **난이도**: 브론즈 2
---
## 2. 핵심 아이디어 (Core Logic)
- 딕셔너리로 효율적인 탐색

---
## 3. 어려웠던 점 (Difficulties)
- 자료구조로 처음에는 리스트를 선택해서 인덱스를 활용해서 소요시간을 구해볼까? 생각했다. 리스트의 모든 값을 탐색하는 것보다 딕셔너리의 키 값으로 한 번에 뽑아내는 것이 효율적일 것 같아, 딕셔너리를 만들어보았다. 그런데 결과적으로는 다시 리스트를 순회하고 있었다.
  - 딕셔너리의 키값으로 알파벳 문자열을 사용한 게 문제였다.
  - 키값으로 처음부터 알파벳 한 글자를 넣었어야 했다.


---
## 4. 새롭게 배운 점 (What I Learned)
- 딕셔너리의 효율성은 '어떤 값을 key로 두는가'에 따라 결정된다.
  - 탐색하려는 대상을 key로 만들어야 딕셔너리의 성능을 제대로 활용할 수 있다!

---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
word = input()

# 숫자 n을 누르기 위해 걸리는 시간: n + 1 (초) 

# 각 숫자에 해당하는 알파벳 문자열을 key로, 소요 시간을 value로, 딕셔너리에 담기
# - 빈 딕셔너리를 만든다.
alphabet_time_dict = {}

# - 우선 리스트에 다이얼 알파벳 문자열을 담는다.
dial_alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# - 위 리스트에서 인덱스 0은 숫자 2(소요 시간 3초), 인덱스 1은 숫자 3(소요 시간 4초), ... 에 해당한다.

# - 소요 시간을 담을 변수를 2로 초기화한다.
processing_time = 2

# - 위 리스트를 순회하며 소요시간을 value 값으로 딕셔너리에 추가한다.
for dial_characters in dial_alphabet_list:
    processing_time += 1
    alphabet_time_dict[dial_characters] = processing_time

# 입력받은 단어의 각 글자가 alphabet_time_dict의 어떤 key에 해당하는지 찾아 그 밸류값을 더한다.
total_time = 0  # 소요 시간을 담을 변수를 0으로 초기화한다.

for char in word:
    for alphabet_str in dial_alphabet_list:
        if char in alphabet_str:
            total_time += alphabet_time_dict[alphabet_str]

print(total_time)
```

- 리스트를 순회하는 반복문을 줄이기 위해, 처음부터 알파벳 한 글자를 키값으로 딕셔너리를 만든다.

- 개선한 코드
```python
word = input()

# 알파벳을 key로, 소요 시간을 value로, 딕셔너리에 담기
# - 빈 딕셔너리를 만든다.
alphabet_time_dict = {}

# - 우선 리스트에 다이얼 알파벳 문자열을 담는다.
dial_alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

# - 위 리스트에서 인덱스 0은 숫자 2(소요 시간 3초), 인덱스 1은 숫자 3(소요 시간 4초), ... 에 해당한다.

# - 소요 시간을 담을 변수를 2로 초기화한다.
processing_time = 2

# - 위 리스트를 순회하며 알파벳 한 글자를 key로, 소요시간을 value로, 딕셔너리에 추가한다.
for dial_characters in dial_alphabet_list:
    processing_time += 1
    for alphabet in dial_characters:
        alphabet_time_dict[alphabet] = processing_time


# 입력받은 단어의 각 글자를 키로 alphabet_time_dict의 밸류(소요 시간)에 접근한다.
total_time = 0  # 소요 시간을 담을 변수를 0으로 초기화한다.

for char in word:
    total_time += alphabet_time_dict[char]

print(total_time)
```