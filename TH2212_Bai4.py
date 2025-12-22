def so_lon_nhat(a, b, c):
    LN=a
    if b > LN:
        LN=b
    if c > LN:
        LN=c
    return LN
def so_nho_nhat(a, b, c):
    NN=a
    if b < NN:
        NN=b
    if c < NN:
        NN=c
    return NN
a = float(input("Nhập số thứ nhất:"))
b = float(input("Nhập số thứ hai:"))
c = float(input("Nhập số thứ ba:"))
ket_qua1 = so_lon_nhat(a, b, c)
ket_qua2 = so_nho_nhat(a, b, c)
print(f"Số lớn nhất trong ba số {a}, {b}, {c} là: {ket_qua1}")
print(f"Số nhỏ nhất trong ba số {a}, {b}, {c} là: {ket_qua2}")