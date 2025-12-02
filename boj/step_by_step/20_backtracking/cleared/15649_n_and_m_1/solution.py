N, M = map(int, input().split())
# 목표: 1~N 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하기

sequence = [num for num in range(1, N+1)]


visited = [False] * (N+1)

def print_sub(current_sub):

    if len(current_sub) == M:  # M개 다 고르면
        print(*current_sub)  # 결과 리스트 언패킹하여 출력
        return
    
    for num in sequence:  # 주어진 N개의 숫자 하나씩 꺼내기
        if not visited[num]:  # 방문한 적 없으면
            visited[num] = True  # 방문했다고 표시
            print_sub(current_sub + [num]) # 결과 리스트에 추가하고, 2개째 선택
            # 방문한 적 있으면, 패스

            # 다녀와서 직전 방문 없었던 일로 하고 다시 탐색
            visited[num] = False

print_sub([])