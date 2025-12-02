T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  # N은 숫자의 개수, K는 크기 순서 (K번째로 큰 수 구하기)
    numbers = input()
    # 목표: 비밀번호(보물상자에 적힌 숫자로 만들 수 있는 모든 수 중 K번째로 큰 수를 10진법으로 변환하여 출력)
    # 한 변에 N/4개의 숫자 배치. N/4 회전 돌리면 처음과 같음.
    # 숫자배열을 두 번 반복한 문자열 생성
    numbers_numbers = numbers*2
    number_list = []  # 회전하면서 만든 수를 리스트에 담기
    for rotation_cnt in range(N//4):  # i는 회전 수
        # 0 회전에서 시작 인덱스는 0, N/4, 2*N/4, 3*N/4. ....
        # 1 회전에서 시작 인덱스는 1, 1+N/4, ...
        for idx in [0, N//4, 2*N//4, 3*N//4]:
            start_idx = rotation_cnt + idx
            number_list.append(numbers_numbers[start_idx:start_idx+N//4])
    # 중복된 수 제거
    number_set = set(number_list)
    decimal_list = list(map(lambda x: int(x, 16), number_set))
    # 내림차순 정렬
    decimal_list.sort(reverse=True)

    print(f'#{tc}', end=' ')
    print(decimal_list[K-1])


