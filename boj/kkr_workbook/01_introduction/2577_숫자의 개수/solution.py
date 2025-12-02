a = int(input())
b = int(input())
c = int(input())

# 각 숫자가 몇 번 쓰였는지 세야 하므로 한 글자씩 쪼개서 리스트로 변환
result = list(str(a * b * c))

# 0부터 9까지 각각 몇번 쓰였는지 한 줄에 하나씩 출력
# 해당 숫자를 인덱스로 하고, 해당 숫자의 개수를 값으로 하는 리스트를 만든다.(0으로 초기화)
num_count_list = [0] * 10
for num in result:
    # num 을 다시 숫자로 변환해서, 인덱스로 값을 추가한다.
    num_count_list[int(num)] += 1

for count in num_count_list:
    print(count)

