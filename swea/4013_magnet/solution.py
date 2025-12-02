# 목표: 4개 자석의 자성 정보가 주어지고, 1칸씩 K번 회전시킨 후, 획득하는 점수를 구하라.
# 모든 회전 끝난 후, 채점
# 1칸 회전 후, 붙어 있는 자석과 자성이 다르면 반대방향으로 1칸 회전
# 각 자석은 8개의 날을 가짐.. (날의 자성은 N극이 0, S극이 1) (그림의 화살표 위치부터 시계 방향)
# 회전 방향은 시계방향이 1, 반시계방향이 -1

from collections import deque   # 리스트를 회전시키기 위해 덱 자료구조 사용
T = int(input())
for tc in range(1, T+1):
    K = int(input())  # 회전시킬 수
    magnet_four = [deque(map(int, input().split())) for _ in range(4)]  # 자석 4개의 자성 정보 2차원 배열
    for rotation_num in range(K):
        m_num, direction = map(int, input().split())  # 회전시킬 자석 번호, 회전 방향
        rotation_list = [0] * 4  # 1번부터 4번까지 회전 정보를 담을 리스트 (동시에 회전시켜야 함.)
        m_idx = m_num - 1
        rotation_list[m_idx] = 1
        i = m_idx  # while문 안에서 변경할 변수
        # 왼쪽 자석들 체크
        while i > 0:
            if magnet_four[i-1][2] != magnet_four[i][6]:  # 왼쪽이랑 자성 다르면
                rotation_list[i-1] = (-1)*rotation_list[i] # rotation_list에 -1 저장
                i -= 1  # 왼쪽 방향으로 계속 체크
            else:  # 자성 같으면 반복 종료
                break
        i = m_idx
        while i < 3:
            if magnet_four[i][2] != magnet_four[i+1][6]:  # 오른쪽이랑 자성 다르면
                rotation_list[i+1] = (-1)*rotation_list[i]
                i += 1  # 오른쪽 방향으로 계속 체크
            else:
                break

        for idx, rotation in enumerate(rotation_list):  # 회전 정보 인덱스와 함께 꺼내기
            magnet_four[idx].rotate(rotation*direction)  # 덱 자료구조의 rotate 메서드로 회전
            

    
    # 회전 끝난 후 채점
    score = 0
    for i in range(4):
        if magnet_four[i][0] == 1:
            score += 2 ** i

    print(f'#{tc} {score}')
