import math
n = int(input("Nhập số nguyên dương n:"))
if n <= 0:
    print("Hãy nhập n > 0")
else:
    tong = math.sqrt(3)
    for i in range(2, n+1):
        tong = math.sqrt(3 + tong)
    print(f"S4({n})= {tong}")