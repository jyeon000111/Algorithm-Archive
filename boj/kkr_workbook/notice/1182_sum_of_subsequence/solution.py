N, S = map(int, input().split())
num_arr = list(map(int, input().split()))  # N개의 정수로 이루어진 수열
# 목표: 크기가 양수인 부분수열 중 그 수열의 원소를 더한 값이 S가 되는 경우의 수 출력

result = []
visited = [False] * (N+1)  # 해당 인덱스의 숫자를 사용했는지 여부 기록 -> 중복 제외
ans_cnt = 0

def cnt_sub(cnt, sum):
    '''고려한 숫자의 개수와 현재까지의 합을 인자로 받아
    부분수열을 구하고
    원소의 합이 S인 경우를 카운트하는
    함수입니다.
    '''
    global ans_cnt
    if sum == S:
        ans_cnt += 1
        return
    elif cnt > N:
        return

    for idx in range(N):
        if visited[idx]:  # 방문한 적이 있다면
            continue # 다음으로 넘어가기
        # 방문한 적이 없다면
        result.append(num_arr[idx])  # 숫자를 결과에 추가하고
        visited[idx] = True

        cnt_sub(cnt+1, sum + num_arr[idx])
        # 재귀호출 다녀와서 원상복구
        result.pop()
        visited[idx] = False

cnt_sub(0, 0)

print(ans_cnt)