N, B = map(int, input().split())
# 목표: 10진법 수 N을 B진법으로 바꿔 출력하기

# 10 이상의 숫자는 알파벳 대문자로 표기함. 대응하는 알파벳을 딕셔너리에 담는다.
decimal_to_alpha_dict = {}
# print(ord('A'))  # 65 -> ord_num에서 55를 빼면 key로 입력할 숫자가 됨.
for ord_num in range(ord('A'), ord('Z')+1):
    decimal_to_alpha_dict[ord_num - 55] = chr(ord_num)

# B로 나눈 나머지를 문자열로 이어붙여 뒤집어서 출력하면 됨.
# -> 1 이하가 될 때까지 반복해서 나눠줘야 함.

# 재귀함수로 풀기
def decimal_to_base(num, base):
    # 이어붙여줘야 하므로, 결과로 나온 숫자를 모두 str로 변환해야 한다.
    # 단, 나머지가 10 이상이면 딕셔너리에서 알파벳을 찾아서 바꿔줘야 한다.
    # 종료 조건: num < base
    if num < base:
        if num >= 10:
            num = decimal_to_alpha_dict[num]
        return str(num)
    # (다음 숫자를 base로 나눈 나머지) + (현재 숫자를 base로 나눈 나머지)
    # 여기서, 다음 숫자는 (현재 숫자를 base로 나눈 몫)
    remainder = num % base
    if remainder >= 10:
        remainder = decimal_to_alpha_dict[remainder]
    return decimal_to_base((num // base), base) + str(remainder)

print(decimal_to_base(N, B))

