## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 1316번]('https://www.acmicpc.net/problem/1316')
  - **난이도**: 실버 5
---
## 2. 핵심 아이디어 (Core Logic)
- set으로 목격한 문자들을 중복 없이 관리하고, 빠르게 탐색한다.
- 재등장한 문자가 직전 문자와 다르다면, 그룹 문자가 아니다. (그 외의 경우는 전부 그룹 문자)

---
## 3. 어려웠던 점 (Difficulties)
- 처음에는 글자가 처음 등장한 위치에서 (해당 문자의 개수 -1) 만큼 떨어진 연속 구간의 끝 위치의 글자가 일치하는지만 확인하면 된다고 판단했다.
  -> 문제는 우연히 맞아떨어지는 경우가 존재한다는 점. 중간에 다른 글자가 끼어드는 걸 알 수 없다.

- 구간 슬라이싱으로 체크해보기로 했다. -> 성공!

- 더 직관적인 다른 방식도 있었다. 목격한 글자들을 set에 담고, set에 이미 있는 글자가 다시 등장하고, 직전 글자와 다르다면 그룹 문자가 아닌 것으로 판단할 수 있다.

---
## 4. 새롭게 배운 점 (What I Learned)
- enumerate 함수 사용법 -> 인덱스와 요소값을 한번에 꺼내 쓸 수 있다.
  `for 인덱스, 요소 in enumerate(반복 가능 객체):`

- 리스트보다 set이 탐색이 훨씬 빠르다. 
  - 리스트는 순서대로 하나씩 넘기면서 탐색. (선형 탐색)
  - set은 사전에서 단어를 찾는 것처럼 직접 접근함. (해시 테이블)
  - 결론: 순서 필요 없고, 중복 허용하지 않고, 무언가 빠르게 찾아야 할 때 set이 최고의 선택

- 헷갈리는 포인트: 속도를 결정하는 건 시퀀스 여부가 아니다!
  - 내부적으로 해시 테이블을 사용하는지 여부가 속도를 결정한다. (set, dict)

---
## 5. 코드 개선 (Refactoring)
1. 오답 코드 (구간의 끝 문자만 확인 -> 허점 발생)
```python
# 목표: 그룹 단어의 개수를 센다.
count_group_word = 0

for _ in range(n):
    word = input()
    # set으로 변환해서 단어에 등장하는 문자의 종류를 중복 없이 구한다.
    char_set = set(word)

    # 현재 단어의 그룹 단어 여부를 True로 초기화한다.
    is_group_word = True

    # char_set의 모든 문자를 탐색한다.
    for char in char_set:
        # 단어에서 해당 문자가 처음 등장하는 인덱스를 구한다.
        first_idx = word.index(char)
        # 단어에서 해당 문자의 개수를 구한다.
        char_count = word.count(char)

        # 연속적으로 쓰였는지 확인한다.
        # (개수-1)만큼 떨어진 인덱스의 요소가 같은 문자가 맞는지 체크
        # - 맞다면, 나머지 문자도 체크한다.
        if word[first_idx + char_count - 1] == char:
            continue
        # 아니라면, 그룹 단어 여부를 False로 재할당하고 반복문을 종료한다.
        else:
            is_group_word = False
            break

    if is_group_word:
        count_group_word += 1

print(count_group_word)
```

- 논리적 허점 발생. 구간의 끝 문자만 확인하는 경우, 중간에 다른 문자가 섞여 있어도 알 수 없음.
- 슬라이싱해서 구간 전체 비교하는 것으로 변경.

2. 개선한 코드 (슬라이싱 활용 -> 구간 전체 비교)
```python
        # 연속적으로 쓰였는지 확인한다. 
        # 개수만큼 떨어진 인덱스까지 슬라이싱해서 같은 문자로 이루어진 문자열인지 체크!
        if word[first_idx:(first_idx + char_count)] == char * char_count:
            continue
        # 아니라면, 그룹 단어 여부를 False로 재할당하고 반복문을 종료한다.
        else:
            is_group_word = False
            break
```

3. 최종 개선 코드 
```python
    # 등장한 문자를 담을 빈 세트를 만든다. 
    seen_char_set = set()
    # 단어에서 한 글자씩 탐색한다. enumerate 함수로 인덱스 변수를 같이 가져간다.
    for idx, char in enumerate(word):
        # 처음 보는 글자면, seen_char_set에 추가한다.
        if char not in seen_char_set:
            seen_char_set.add(char)
        # 다시 등장한 단어면, 직전 글자와 같은지 체크한다.
        # -> 다르면 그룹 단어가 아니다!
        elif char != word[idx - 1]:
            is_group_word = False
            break
```
  