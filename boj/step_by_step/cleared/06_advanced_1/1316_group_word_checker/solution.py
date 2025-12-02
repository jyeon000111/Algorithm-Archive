# 단어의 개수 n을 입력받는다.
n = int(input())

# 단어에서 한 문자가 연속적으로 쓰이지 않고, 다시 등장하면 그룹 단어가 아니다.
# 목표: 그룹 단어의 개수를 센다.
count_group_word = 0

for _ in range(n):
    word = input()
    # 현재 단어의 그룹 단어 여부를 True로 초기화한다.
    is_group_word = True

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

    if is_group_word:
        count_group_word += 1

print(count_group_word)



        