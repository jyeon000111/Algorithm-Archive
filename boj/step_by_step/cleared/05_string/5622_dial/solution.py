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