from datetime import datetime, timedelta

print("Bai 9: Xu ly thoi gian")

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau

print("Bat dau:", bat_dau.strftime("%d/%m/%Y %H:%M"))
print("Ket thuc:", ket_thuc.strftime("%d/%m/%Y %H:%M"))
print("Thoi luong:", thoi_luong)

thoi_gian_tiep_theo = bat_dau + timedelta(minutes=30)
print(
    "Sau 30 phut:",
    thoi_gian_tiep_theo.strftime("%d/%m/%Y %H:%M")
)
