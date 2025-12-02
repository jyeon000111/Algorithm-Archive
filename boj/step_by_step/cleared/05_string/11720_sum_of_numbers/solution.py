n = int(input())

# n개의 숫자가 공백 없이 쓰여있다.
# 문자열로 받아서, map 함수로 한글자씩 int로 변환

num_string = input()
print(sum(map(int, num_string)))
