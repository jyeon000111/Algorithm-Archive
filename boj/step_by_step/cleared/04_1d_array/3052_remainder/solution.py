# The "What" (최종 코드)

# 나머지를 담을 빈 리스트를 생성한다.
num_list = []

# 수 10개를 입력받는다. 42를 나눈 나머지를 구한다.
for _ in range(10):
    num = int(input())
    num_list.append(num % 42)


# 서로 다른 값이 몇 개 있는지 출력한다.
# - set으로 변환해서 중복을 제거한 뒤, len으로 길이를 구한다.
print(len(set(num_list)))