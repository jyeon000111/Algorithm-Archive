# 대소문자 구분 없이 가장 많이 사용된 알파벳을 대문자로 출력한다.
# (단, 가장 많이 사용된 알파벳이 여러 개면 ? 출력)

word = input().upper() # 처음부터 모두 대문자로 바꾼다.

# 빈 딕셔너리를 만든다. ((알파벳: 개수) 쌍을 추가할 예정)
alphabet_count_dict = {}

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