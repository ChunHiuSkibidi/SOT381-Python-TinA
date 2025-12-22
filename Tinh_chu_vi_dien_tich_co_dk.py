while True:
  w = float(input("Nhập chiều dài: "))
  if 0 <= w <= 100:
      break
  else:
      print("Sai, nhập lại")
while True:
  h = float(input("Nhập chiều rộng:"))
  if 0 <= h <= 100:
      break
  else:
      print("Sai, nhập lại")      

chuvi = (w + h) * 2
dt = w * h
print(f"Chu vi HCN là:{chuvi:.2f}")
print(f"Diện tich HCN là:{dt:.2f}")
