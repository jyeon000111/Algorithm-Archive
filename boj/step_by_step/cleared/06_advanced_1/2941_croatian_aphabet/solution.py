# 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는가
word = input()

# 크로아티아 알파벳 리스트를 만든다.
cro_alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 주어진 단어에서 크로아티아 알파벳을 찾아 한 글자로 바꿔준다.
for cro_alpha in cro_alpha_list:
    word = word.replace(cro_alpha, '*')

# 변경된 문자열의 길이를 출력한다.
print(len(word))
