# 팰린드롬: 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어
# 팰린드롬이면 1, 아니면 0을 출력한다.
word = input()
word_reversed = word[::-1]

if word == word_reversed:
    print(1)
else:
    print(0)