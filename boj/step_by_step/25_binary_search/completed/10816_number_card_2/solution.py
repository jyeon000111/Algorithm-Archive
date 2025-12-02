# 상근이가 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적힌 숫자 카드를 몇 개 보유하고 있는지 출력
# - lower bound(숫자의 시작 위치) 와 upper bound(숫자의 끝 바로 다음 위치)를 찾아서 차를 구해주면 된다.
# - left가 lower bound에서 멈추고, right가 upper bound 에서 멈추게 할 수 있나?
# -> 일단 따로 구해보자.

def lower_bound(left, right, k):
    '''
    숫자의 시작 위치를 찾아 반환한다.
    '''

    while left < right:
        mid = (left + right) // 2
        # k가 오른쪽에 있는 경우
        if k > cards[mid]:
            left = mid + 1
        # k가 왼쪽에 있거나 같은 경우
        else:
            right = mid

    return right

def upper_bound(left, right, k):
    '''
    숫자의 끝 바로 다음 위치를 찾아 반환한다.
    '''

    while left < right:
        mid = (left + right) // 2
        # k가 오른쪽에 있거나 같은 경우
        if k >= cards[mid]:
            left = mid + 1
        # k가 왼쪽에 있는 경우
        else:
            right = mid

    return right

N = int(input())
cards = list(map(int, input().split()))  # 상근이가 가진 숫자 카드 리스트
M = int(input())
target_list = list(map(int, input().split()))  # 탐색할 정수 목록

# 이진 탐색을 위해 오름차순 정렬
cards.sort()  # [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]

for target in target_list:
    lower = lower_bound(0, N, target)
    upper = upper_bound(0, N, target)
    print(upper - lower, end=' ')