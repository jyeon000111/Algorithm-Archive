total_price = int(input())
n = int(input())
real_total_price = 0
for i in range(n):
    price, count = map(int, input().split())
    real_total_price += price * count

if total_price == real_total_price: 
    print("Yes")
else:
    print("No")