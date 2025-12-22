def tinhS(n):
    TS=0
    for i in range(1, n + 1):
        TS += i
    MS=0
    for i in range(1, n // 2 + 1):
        MS += 2 * i        
    S = TS / MS
    return S
n = int(input("Nhập số n:"))
kq = tinhS(n)
print(f"Kết quả tổng S là:{kq}")