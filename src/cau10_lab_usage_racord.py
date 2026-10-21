from datetime import datetime

print("Bai 10: Lab Usage Record")

ma_phien = input("Nhap ma phien: ")
phong = input("Nhap phong may: ")
cong_suat_w = float(input("Nhap cong suat may (W): "))
so_phut = float(input("Nhap thoi gian su dung (phut): "))
gia_dien_kwh = float(input("Nhap gia dien (VND/kWh): "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * gia_dien_kwh
thoi_diem = datetime.now()

print("\n===== LAB USAGE RECORD =====")
print("Ma phien:", ma_phien)
print("Phong may:", phong)
print("Cong suat:", f"{cong_suat_w:.0f} W")
print("Thoi gian su dung:", f"{so_phut:.0f} phut")
print(f"Dien nang: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi:.0f} VND")
print(
    "Thoi diem ghi nhan:",
    thoi_diem.strftime("%d/%m/%Y %H:%M:%S")
)
print("============================")
