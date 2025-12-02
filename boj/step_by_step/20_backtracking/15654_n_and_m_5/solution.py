N, M = map(int, input().split())  # N은 수의 개수, M은 수열의 길이
num_arr = list(map(int, input().split()))
# 주어진 수를 오름차순 정렬
num_arr.sort()

result_list = []
visited = [False] * N  # 배열의 해당 인덱스의 값을 수열에 사용했는지 체크

# 목표: 길이가 M인 수열 모두 출력. 사전 순으로 출력. 중복된 숫자 허용 X
def subsequence(n):
    '''리스트의 길이를 인자로 받아
    길이가 M이 될 때까지 채우고,
    출력하는 함수입니다.
    '''
    if n == M:  # 길이가 M이 되면 출력하고 return으로 종료
        print(*result_list)
        return

    for idx in range(N):  # 인덱스로 원본 숫자배열에 접근
        if visited[idx]:  # 사용한 값이면
            continue
        else:  # 사용하지 않은 값이면
            result_list.append(num_arr[idx])  # 수열에 추가
            visited[idx] = True
            subsequence(n+1)  # 재귀 호출

            result_list.pop() # 돌아와서 흔적 지우기
            visited[idx] = False


subsequence(0)
