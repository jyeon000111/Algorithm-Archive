# 문제 출처
https://www.acmicpc.net/problem/2480

---
# 내 아이디어

- 같은 눈 3개일 때는 상금 구하기 쉬움.
- 문제는 같은 눈 2개일 때, 같은 눈이 무엇인지 알아내는 것.
- 또 모두 다른 눈이 나올 때, 그 중 가장 큰 눈이 무엇인지 알아내는 것. sorted 함수 활용?

---
# 새로 배운 것
1. 가장 큰 값을 찾는 방법
   - max() 함수: 숫자들을 넣어주면 가장 큰 값을 찾아줌.
     - max(1, 2, 3) = 3
   - if 조건문으로 비교(기본 원리)
      ```python
      a, b, c = 10, 30, 20

      # a가 가장 크다고 가정하고 b, c와 비교
      if a >= b and a >= c:
          largest = a
      # a가 아니라면, b가 가장 크다고 가정하고 c와 비교
      elif b >= a and b >= c:
          largest = b
      # a, b 둘 다 아니면 c가 가장 큼
      else:
          largest = c

      print(largest) # 출력: 30
      ```

2. 3개 중 같은 숫자가 딱 2개일 때, 같은 숫자 뽑아내는 방법
   - `if` 조건문으로 직접 비교하기
      ```python
      a, b, c = map(int, input().split())

      if a == b and a != c:
          print(a)
      elif b == c and b != a:
          print(b)
      elif c == a and c != b:
          print(c)
      ```
    - 정렬(sorted 함수) 활용하기
        숫자 3개를 리스트에 넣고 **정렬**한다.

        1.  숫자 3개를 정렬하면, 같은 숫자는 반드시 붙어있게 돼.
        2.  만약 세 숫자가 모두 다르거나, 모두 같다면 이 방법으로 걸러낼 수 있어.

        <!-- end list -->

        ```python
        nums = sorted(list(map(int, input().split()))) # 입력받자마자 리스트로 만들고 정렬

        # 1. 세 숫자가 모두 같은 경우는 제외
        # 2. 정렬했기 때문에, 가운데 숫자(nums[1])가 양 옆과 다르면 세 숫자가 모두 다른 것
        if nums[0] == nums[2]: # nums[0]와 nums[2]가 같으면 세 숫자가 모두 같은 것
            pass # 아무것도 안함
        elif nums[0] == nums[1]: # 왼쪽 두 개가 같으면
            print(nums[0])
        elif nums[1] == nums[2]: # 오른쪽 두 개가 같으면
            print(nums[1])
        ```

        이 방법은 가운데 값(`nums[1]`)이 핵심이라는 점을 이용

# 보완된 코드

```python
else:
    if a == b or a == c:
        equal_num = a
    else:
        equal_num = b
    print(1000 + equal_num * 100)
```

이 부분을 \*\*정렬(sort)\*\*을 이용하면 한 줄로 바꿀 수 있어.

숫자 3개를 정렬하면, 같은 숫자가 2개일 경우 \*\*그 숫자는 항상 가운데(`index 1`)\*\*에 위치하게 돼.

  * `[5, 2, 5]` → 정렬하면 → `[2, 5, 5]`
  * `[5, 5, 2]` → 정렬하면 → `[2, 5, 5]`
  * `[2, 5, 5]` → 정렬하면 → `[2, 5, 5]`

어떤 경우든 가운데 숫자는 `5`지? 이 원리를 이용하는 거야.

### 수정 코드 예시

```python
a, b, c = map(int, input().split())

if a == b == c:
    # 1. 모두 같은 눈
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    # 2. 2개만 같은 눈 (정렬해서 가운데 값 사용)
    equal_num = sorted([a, b, c])[1]
    print(1000 + equal_num * 100)
else:
    # 3. 모두 다른 눈
    print(max(a, b, c) * 100)
```

**정렬 트릭**