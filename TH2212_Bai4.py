def so_lonnho_nhat(a, b, c):
    LN=a
    if b > LN:
        LN=b
    if c > LN:
        LN=c
        
    NN=a
    if b < NN:
        NN=b
    if c < NN:
        NN=c
    return LN, NN
a = float(input("Nhập số thứ nhất:"))
b = float(input("Nhập số thứ hai:"))
c = float(input("Nhập số thứ ba:"))
ket_qua1, kq2 = so_lonnho_nhat(a, b, c)

print(f"Số lớn nhất trong ba số {a}, {b}, {c} là: {ket_qua1}")
print(f"Số nhỏ nhất trong ba số {a}, {b}, {c} là: {kq2}")