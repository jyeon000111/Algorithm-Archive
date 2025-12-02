N = int(input())
# 목표: N개의 원판을 1번 장대에서 3번 장대로 옮길 때, 최소 이동 횟수와 이동 순서를 출력
# 규칙1: 한 번에 1개만 옮길 수 있다. 
# 규칙2: 쌓은 원판은 위의 것이 아래보다 작아야 한다.

move_cnt = 0
# 이동 횟수 다음에 이동 순서를 출력해야 하므로, 리스트에 튜플로 저장한다.
result_list = []


def move_disk(N, start_pole, target_pole):
    '''옮길 원판의 개수 N과, 원판이 현재 있는 시작 장대, 목표 장대를 인자로 받아
    N개의 원판을 1번에서 3번으로 옮기는 과정을
    출력하는 함수입니다.
    '''
    global move_cnt

    empty_pole = 6 - start_pole - target_pole

    if N == 1:  # 종료 조건: 원판이 1개일 때만 실제로 이동할 수 있다.
        move_cnt += 1  # 이동 횟수 1 증가
        result_list.append((start_pole, target_pole))  # 이 때의 이동 순서를 결과 리스트에 추가
        return

    # N 개의 원판을 3번으로 옮기는 과정은
    # - N-1 개의 원판을 2번으로 옮기고, 가장 큰 원판을 3번으로 옮긴 다음,
    # - 다시 N-1개의 원판을 2번에서 3번으로 옮기는 과정 과 같다.

    move_disk(N-1, start_pole, empty_pole)
    move_disk(1, start_pole, target_pole)
    move_disk(N-1, empty_pole, target_pole)

move_disk(N, 1, 3)
print(move_cnt)
for item in result_list:
    print(*item)