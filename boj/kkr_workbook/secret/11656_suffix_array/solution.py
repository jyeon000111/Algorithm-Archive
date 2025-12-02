# 목표: 문자열 s의 모든 접미사를 사전순으로 정렬한 다음 출력
S = input()
N = len(S)  # 문자열의 길이

tail_list = []
for i in range(N):
    tail = S[i:]
    tail_list.append(tail)



# 정렬 기준은 첫 글자의 아스키코드
# 첫 글자가 같은 경우, 두번째 글자도 정렬해야 함..
while True:
    tail_list.sort(key=lambda x: ord(x[i]))
    ith_char_set = []
    for

print(tail_list)