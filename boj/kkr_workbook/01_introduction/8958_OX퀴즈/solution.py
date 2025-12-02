T = int(input())
for test_case in range(T):
    ox_result = input()
    # O는 1점, 연속 정답이면 1점씩 가산됨.
    # X는 0점
    # X를 기준으로 문자열을 분리한다.
    splited_result = ox_result.split('X')
    
    score = 0
    for chars in splited_result:
        # 빈문자열은 생략
        if chars == '':
            continue
        # 빈문자열 아닐 때 O의 길이를 구한다. 
        # (1~길이)까지 합을 구하면, 해당 문자열의 점수가 된다.
        else:
            o_length = len(chars)
            for num in range(o_length + 1):
                score += num
    print(score)