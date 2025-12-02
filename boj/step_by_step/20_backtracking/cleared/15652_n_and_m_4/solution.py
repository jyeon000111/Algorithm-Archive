N, M = map(int, input().split())

# 목표: 1~N 자연수 중 M개를 고른 수열 출력
# 조건1: 중복 허용
# 조건2: 비내림차순 A1 <= A2 <= .. <= Am
# -> 탐색 시작점 start를 인자로 받는 함수 만들기

result = []

def print_seq(start):
    '''탐색 시작점을 인자로 받아
    길이 M인 비내림차순 정렬 수열을 출력하는 함수입니다.
    '''
    if len(result) == M:
        print(*result)
        return

    for num in range(start, N+1):
        result.append(num)
        print_seq(num)  # 현재 결과리스트에 추가한 숫자부터 다시 탐색
        result.pop()
    

print_seq(1)

