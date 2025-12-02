s = input() # 소문자로만 이루어진 단어

for ord_num in range(ord('a'), ord('z')+1):
    current_char = chr(ord_num)
    # 현재 알파벳이 단어에서 처음 등장하는 인덱스를 출력한다.
    # find 메서드 활용 (없는 경우 -1 반환)
    print(s.find(current_char), end=' ')