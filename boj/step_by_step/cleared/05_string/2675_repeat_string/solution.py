T = int(input())

for testcase in range(T):
    # 문자열 s의 각 문자를 r번 반복해 새 문자열 p를 만든다.
    r_str, s = input().split()
    r = int(r_str)
    # 문자열 조각들을 담을 빈 리스트를 만든다.
    p_list = []
    # s의 각 문자를 순회하며 r을 곱해 p_list에 담는다.
    for char in s:
        p_list.append(char * r)
    
    # join 메서드로 리스트의 조각들을 공백 없이 합친다.
    p = ''.join(p_list)
    print(p)
