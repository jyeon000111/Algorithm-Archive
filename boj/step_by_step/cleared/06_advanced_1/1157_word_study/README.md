## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 1157번]('https://www.acmicpc.net/problem/1157')
  - **난이도**: 브론즈 1
---
## 2. 핵심 아이디어 (Core Logic)
- 딕셔너리 활용

---
## 3. 어려웠던 점 (Difficulties)
- 딕셔너리를 잘 만들어놓고, 제대로 활용하기가 어려웠다. 계속 리스트를 새로 만들고 있는 나 자신... 코드가 길고 복잡해졌다.

---
## 4. 새롭게 배운 점 (What I Learned)
- 딕셔너리의 `.items()` 메서드를 활용하면, key, value를 한 번에 가져올 수 있어 코드가 훨씬 직관적이다.
```python
for key, value in my_dict.items():
```

- 딕셔너리의 `.get(key[, default 없을 때 반환할 값])` 메서드에서 default는 키워드 인자가 아닌 위치 인자다.


---
## 5. 코드 개선 (Refactoring)
- 이전 코드
```python
alphabet_count_dict = {}

for char in word:
    # 딕셔너리에 해당 문자가 키 값으로 존재하지 않으면, 밸류를 1로 하는 쌍을 새로 추가한다.
    if alphabet_count_dict.get(char) is None:
        alphabet_count_dict[char] = 1

    # 딕셔너리에 해당 문자가 키 값으로 존재하면 밸류를 1 더해준다.
    else:
        alphabet_count_dict[char] += 1


# (키, 밸류) 를 리스트에 담는다.
alphabet_count_list = []
for key in alphabet_count_dict.keys():
    alphabet_count_list.append((key, alphabet_count_dict[key]))

# 가장 큰 개수를 구한다.
# 튜플의 두번째 값만 리스트에 담아서 최댓값을 구한다.
count_list = [alphabet_count_list[idx][1] for idx in range(len(alphabet_count_list))]
max_count = max(count_list)

# 가장 개수가 많은 알파벳을 리스트에 모두 담는다.
max_count_alphabet = []
for char_and_count in alphabet_count_list:
    if char_and_count[1] ==  max_count:
        max_count_alphabet.append(char_and_count[0])

# 리스트에 담긴 값이 1개이면, 언패킹해서 출력
if len(max_count_alphabet) == 1:
    print(*max_count_alphabet)
# 아니면, ? 출력
else:
    print('?')
```

- .get() 메서드의 default값을 설정해서 if-else문을 간결하게 바꿀 수 있다.
- 리스트를 여러 개 만들지 않고, 딕셔너리 안에서 최대한 해결한다.
  - .keys() , .values(), .items() 메서드 적극 활용.

- 개선한 코드
```python
for char in word:
    # .get()메서드로 해당 글자의 밸류값에 접근한다.
    # 밸류값이 존재하면, 1을 더해서 밸류값을 재설정해준다.
    # 존재하지 않는 경우, default로 0을 설정해서 1이 밸류값으로 설정되어 추가되도록 한다.
    alphabet_count_dict[char] = alphabet_count_dict.get(char, 0) + 1
    
# 밸류값 중 가장 큰 값을 구한다.
max_count = max(alphabet_count_dict.values())

# 밸류값이 max_count인 key를 리스트에 추가한다.
result_list = []
for key, value in alphabet_count_dict.items():
    if value == max_count:
        result_list.append(key)

# result_list의 요소가 1개면 언패킹해서 출력
if len(result_list) == 1:
    print(*result_list)
# 1개가 아니면 ?를 출력
else:
    print('?')
```