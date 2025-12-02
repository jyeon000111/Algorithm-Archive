# 정렬이 아닌 조합으로 풀어보기!
# 목표: 아홉 난쟁이의 키 중에서 합이 100이 되는 크기 7의 조합을 찾아 출력 (오름차순)
# 단, 정답 여러 개인 경우 아무거나 출력

nine_heights = []
for _ in range(9):
    nine_heights.append(int(input()))
nine_heights.sort()  # 오름차순 정렬

result = []
print_flag = False
visited = [False] * 9 # 중복을 허용하지 않으므로 방문 여부 기록

def print_combination(result_cnt, not_in_cnt,  sum):
    '''조합에 넣은 숫자의 개수, 넣지 않은 숫자의 개수, 총합을 인자로 받아
    개수가 7, 총합이 100이 되는 경우를
    출력하는 함수입니다.
    '''
    global print_flag

    if print_flag:
        return
    if not_in_cnt > 2:  # 넣지 않은 숫자가 2개를 넘는 경우 가지치기
        return
    if result_cnt > 7:  # 넣은 숫자가 7개 넘는 경우 가지치기
        return
    if sum > 100:  # 총합이 100이 넘는 경우는 가지치기
        return
    elif sum == 100:  # 총합이 100인 경우
        if result_cnt == 7:  # cnt가 7일 때만 출력
            for num in result:
                print(num)
                print_flag = True

        return

    for idx in range(9):
        if visited[idx]:  # 방문한 경우 다음으로 넘어가기
            continue
        else:
            height = nine_heights[idx]
            # 조합에 넣지 않은 경우
            print_combination(result_cnt, not_in_cnt + 1, sum)

            # 조합에 넣은 경우
            result.append(height)
            visited[idx] = True
            print_combination(result_cnt + 1, not_in_cnt, sum + height)

            # 재귀 다녀와서 원상복구
            result.pop()
            visited[idx] = False

print_combination(0, 0, 0)