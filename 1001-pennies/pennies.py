"""
Start with 1,001 pennies lined up on a table. First, replace every other coin with a
nickel. Next, replace every third coin with a dime. Finally, replace every fourth coin
with a quarter. How much money is on the table now?
"""
from collections import Counter
from decimal import Decimal

QUARTER = Decimal("0.25")
DIME = Decimal("0.10")
NICKEL = Decimal("0.05")
PENNY = Decimal("0.01")

coins = []
for coin in range(1, 1002):
    if coin % 4 == 0:
        coin = QUARTER
    elif coin % 3 == 0:
        coin = DIME
    elif coin % 2 == 0:
        coin = NICKEL
    else:
        coin = PENNY
    coins.append(coin)

print("Coin | Count")
print("------------")
for coin, count in Counter(coins).items():
    print(f"{coin} | {count:}")
print(f"\nTotal: ${sum(coins)}")
