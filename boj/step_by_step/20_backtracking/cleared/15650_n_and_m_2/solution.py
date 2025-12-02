N, M = map(int, input().split())

# 목표: 1~N 자연수 중 중복 없이 M개를 고른 수열 (오름차순)

result = []  # 수열을 담을 리스트

def print_sub(start): 
    '''탐색 시작점을 인자로 받아, 
    길이 M의 수열을 출력하는 함수입니다.
    오름차순으로 수를 중복없이 선택합니다.
    '''
    if len(result) == M:
        print(*result)
        return
    
    for num in range(start, N+1):  # 시작점부터 N 까지 숫자를 하나씩 꺼내기
        result.append(num)  # 첫번째 숫자를 결과 리스트에 담는다.
        # num+1을 시작점으로 하는 탐색을 재귀호출한다.
        print_sub(num + 1)
        result.pop()


print_sub(1)