# The "What" (최종 코드)
num_list = []
for i in range(9):
    number = int(input())
    num_list.append(number)

max_num = max(num_list)
print(max_num)

# 최댓값이 몇 번째 수인지 출력한다. 주어진 수들은 모두 다른 값이다.
max_index = num_list.index(max_num)

print(max_index + 1)
