def so_lon_nhat(a, b, c):
    LN=a
    if b > LN:
        LN=b
    if c > LN:
        LN=c
    return LN
a = float(input("Nhập số thứ nhất:"))
b = float(input("Nhập số thứ hai:"))
c = float(input("Nhập số thứ ba:"))
ket_qua = so_lon_nhat(a, b, c)
print(f"Số lớn nhất trong ba số {a}, {b}, {c} là: {ket_qua}")
    
     