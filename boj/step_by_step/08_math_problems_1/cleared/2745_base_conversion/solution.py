N, B = input().split() 
B = int(B)

# B진법 수 N을 10진법으로 바꿔서 출력한다.

# (알파벳 대문자): (나타내는 숫자) 쌍을 딕셔너리에 담는다.
alpha_num_dict = {}
# print(ord('A'))  # 65이므로, (ord(대문자) - 55) 값을 밸류로 삼는다.
for ord_num in range(ord('A'), ord('Z') + 1):
    alpha_num_dict[chr(ord_num)] = ord_num - 55

# 10진법으로 계산한 결과값을 담을 변수를 0으로 초기화
result = 0

# 편의상 N 문자열을 뒤집어서 계산한다.
N_reversed = N[::-1]
# 인덱스가 곧 제곱의 지수가 된다!
for exponent, char in enumerate(N_reversed):
    if char.isdecimal():
        result += int(char) * (B ** exponent)
    else:
        result += alpha_num_dict[char] * (B ** exponent)

print(result)
