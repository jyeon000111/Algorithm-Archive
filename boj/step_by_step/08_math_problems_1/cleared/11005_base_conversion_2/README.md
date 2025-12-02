## 1. 문제 정보 (Problem)

  - **출처 및 번호**: [백준 11005번]('https://www.acmicpc.net/problem/11005')
  - **난이도**: 브론즈 1
  - **문제 요약**: 10진법 수 N을 B진법으로 바꿔 출력하기

---
## 2. 핵심 아이디어 (Core Logic)
- B로 나눈 나머지를 문자열로 이어붙여 뒤집어서 출력하면 됨.
  -> 1 이하가 될 때까지 반복해서 나눠줘야 함.
  1) 재귀함수
    - 숫자를 키로 알파벳을 밸류로 하는 딕셔너리를 생성한다.
  2) while문
    - 숫자를 인덱스로 알파벳을 요소값으로 하는 문자열을 생성한다.


---
## 3. 어려웠던 점 (Difficulties)
- 문자열과 인덱스를 활용해서, 10 이상의 숫자에 대응하는 알파벳에 접근하도록 하는 방법 -> 알파벳 하나하나 직접 입력하다 오타 나면 큰 일!
`decimal_to_alpha_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
  - -> for 반복문과 ord(), chr() 아스키코드 활용하는 게 정확함.

- 지금은 N이 자연수로 주어져서 0일 때의 엣지케이스 고려 안 해도 됨.
  - 문제 풀 때, 예외적인 입력값이 있는지 항상 체크하는 습관을 들어야 함.

---
## 4. 새롭게 배운 점 (What I Learned)
- 재귀 vs 반복문(while)
  - 재귀는 코드가 간결하고 수학적 정의와 닮음.
  - 반복문은 일반적으로 더 효율적이고 컴퓨터의 동작 방식과 가까움.

---
## 5. 코드 개선 (Refactoring)
1) 방법: 재귀함수
```python
N, B = map(int, input().split())
# 목표: 10진법 수 N을 B진법으로 바꿔 출력하기

# 10 이상의 숫자는 알파벳 대문자로 표기함. 대응하는 알파벳을 딕셔너리에 담는다.
decimal_to_alpha_dict = {}
# print(ord('A'))  # 65 -> ord_num에서 55를 빼면 key로 입력할 숫자가 됨.
for ord_num in range(ord('A'), ord('Z')+1):
    decimal_to_alpha_dict[ord_num - 55] = chr(ord_num)

# B로 나눈 나머지를 문자열로 이어붙여 뒤집어서 출력하면 됨.
# -> 1 이하가 될 때까지 반복해서 나눠줘야 함.

# 재귀함수로 풀기
def decimal_to_base(num, base):
    # 이어붙여줘야 하므로, 결과로 나온 숫자를 모두 str로 변환해야 한다.
    # 단, 나머지가 10 이상이면 딕셔너리에서 알파벳을 찾아서 바꿔줘야 한다.
    # 종료 조건: num < base
    if num < base:
        if num >= 10:
            num = decimal_to_alpha_dict[num]
        return str(num)
    # (다음 숫자를 base로 나눈 나머지) + (현재 숫자를 base로 나눈 나머지)
    # 여기서, 다음 숫자는 (현재 숫자를 base로 나눈 몫)
    remainder = num % base
    if remainder >= 10:
        remainder = decimal_to_alpha_dict[remainder]
    return decimal_to_base((num // base), base) + str(remainder)

print(decimal_to_base(N, B))
```


2) 방법: while문 
```python
# 0부터 35까지 대응하는 문자를 인덱스로 접근할 수 있게 문자열을 생성한다.
decimal_to_alpha_str = ''
for num in range(10):
    decimal_to_alpha_str += str(num)
for ord_num in range(ord('A'), ord('Z')+1):
    char = chr(ord_num)
    decimal_to_alpha_str += char


# 뒤집힌 결과를 담을 빈문자열 생성
reversed_result_str = ''
while True:
    # 종료조건: N이 0 이하가 되면 반복을 끝낸다.
    if N <= 0:
        break
    # 현재의 N을 B로 나눈 값을 변수에 담는다.
    # - decimal_to_alpha_str 문자열을 활용해서 str로 변환한다.
    current_remainder = decimal_to_alpha_str[N % B]
    
    # N에 N을 B로 나눈 몫을 재할당한다.
    N = N // B 
    reversed_result_str += current_remainder

# 결과 출력
print(reversed_result_str[::-1])
```
