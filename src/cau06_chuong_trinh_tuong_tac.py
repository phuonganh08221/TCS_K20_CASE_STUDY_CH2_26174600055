from datetime import datetime

print("Bai 6: Chuong trinh tuong tac")

ma_sinh_vien = input("Nhap ma sinh vien: ")
ten = input("Nhap ten sinh vien: ")
phong = input("Nhap phong hoc: ")

thoi_gian = datetime.now()

print("\n--- THONG TIN ---")
print("Ma sinh vien:", ma_sinh_vien)
print("Ten:", ten)
print("Phong hoc:", phong)
print(
    "Thoi gian ghi nhan:",
    thoi_gian.strftime("%d/%m/%Y %H:%M:%S")
)
