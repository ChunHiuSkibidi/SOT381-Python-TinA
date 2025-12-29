toan = float(input("Nhập điểm môn toán:"))
ly = float(input("Nhập điểm môn lý:"))
hoa = float(input("Nhập điểm môn hóa:"))
tong = toan + ly + hoa
if tong >= 15 and toan >= 4 and ly >= 4 and hoa >= 4:
    print("Đậu")
    if toan >= 5 and ly >= 5 and hoa >= 5:
        print("Học đều các môn")
        else:
            print("Học chua đều các môn")
            
