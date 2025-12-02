price = int(input())  # 지불할 돈
change = 1000 - price  # 거스름돈



# 동전 단위를 리스트에 담는다. (내림차순)
coins = [500, 100, 50, 10, 5, 1]

count_coins = 0  # 동전 개수를 0으로 초기화

# change 값을 coins 리스트의 첫번째 요소로 최대한 빼주면서 동전 개수를 카운트
for coin in coins:
    # 남은 거스름돈이 0원이 되면 반복문 종료!
    if change == 0:
        break
    # 거스름돈보다 현재 동전의 금액이 작거나 같아야 사용 가능!
    while change >= coin:  # while문으로 계속 반복
        change -= coin  # 현재 동전만큼 차감
        count_coins += 1  # 사용한 동전 개수 카운트

print(count_coins)
