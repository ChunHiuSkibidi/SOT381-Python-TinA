a = float(input("Nhập số thứ nhất:"))
b = float(input("Nhập số thứ hai:"))
c = float(input("Nhập số thứ ba:"))
max = a
if b > max:
    max = b
if c > max:
    max = c
print(f"Số lớn nhất là: {max}")
min = a
if b < min:
    min = b
if c < max:
    min = c
print(f"Số nhỏ nhất là: {min}")    
