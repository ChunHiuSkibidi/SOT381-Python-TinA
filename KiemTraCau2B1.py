n = int(input("Nhập số nguyên dương:"))
# kiểm tra đk n
if n < 0:
    print("Hãy nhập n > 0")
else:
#dùng csc số đầu là 2 số cuối là 2n
#cthuc tổng = n*(2 + 2n)/2
    tong = n * (2 + 2*n) // 2
    print(f"S2={tong} với n={n}")