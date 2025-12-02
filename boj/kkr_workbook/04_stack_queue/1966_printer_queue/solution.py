T = int(input())
for _ in range(T):
    N, M = map(int, input().split())  # N은 문서의 개수
    # M은 몇 번째로 인쇄되었는지 궁금한 문서가 놓여있는 인덱스
    priority_list = list(map(int, input().split()))  # N개 문서의 중요도 리스트

    # 순서 그대로 두고, 인쇄순서 파악하는 법?
    # 리스트에서 처음 나오는 max값이 먼저 인쇄된다. (인쇄된 인덱스 새 리스트에 기록)
    # 뒤 인덱스부터 다시 max값 탐색 -> 없으면 0번 인덱스부터 탐색


    search_idx = 0  # 탐색 기준 인덱스를 0으로 초기화

    # 리스트에서 탐색해야 하는 중요도 순서 (내림차순 정렬)
    print_order_list = sorted(priority_list, reverse = True)
    i = 0  # 타겟 인덱스

    print_cnt = 0  # 인쇄 횟수 카운트 변수

    print_idx_list = []  # 인쇄된 인덱스를 기록하는 리스트

    while True:
        target = print_order_list[i]  # i를 1씩 증가시키며, print_order_list에서 타겟을 꺼낸다.
        try:  # search_idx 기준으로 뒷 부분부터 탐색
            print_idx = priority_list.index(target, search_idx)
        except:  # 없으면 앞 부분 탐색
            print_idx = priority_list.index(target, 0, search_idx)
        print_idx_list.append(print_idx)  # 인쇄된 인덱스 기록
        print_cnt += 1  # 인쇄 횟수 1 증가
        search_idx = print_idx + 1  # 인쇄한 인덱스 바로 뒤 인덱스를 기준 인덱스로 재설정
        i += 1

        # M번 인덱스 인쇄되면 반복문 종료
        if print_idx == M:
            break

    print(print_cnt)



