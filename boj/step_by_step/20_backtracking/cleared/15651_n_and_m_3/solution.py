N, M = map(int, input().split())

# 목표: 1~N 자연수 중에서 길이가 M인 수열을 모두 출력 (중복 허용)
result = []  # 수열을 담을 리스트

def print_seq(cnt):
    if cnt == M:
        print(*result)
        return
    
    for num in range(1, N+1):
        result.append(num)
        print_seq(cnt+1)
        result.pop()
    
print_seq(0)