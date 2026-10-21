print("Bai 4: Tinh dien nang tieu thu")

cong_suat_w = 250
gia_dien_kwh = 3000

so_phut = 90
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * gia_dien_kwh

print("Cong suat:", cong_suat_w, "W")
print("Thoi gian:", so_phut, "phut")
print(f"Dien nang tieu thu: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi:.0f} VND")

so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * gia_dien_kwh

print("Thoi gian:", so_phut, "phut")
print(f"Dien nang tieu thu: {dien_nang_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi:.0f} VND")
