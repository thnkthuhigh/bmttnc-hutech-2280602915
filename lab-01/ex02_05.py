sogiolam = float(input("Nhap so gio lam moi tuan: "))
luonggio = float(input("Nhap thu lao tren moi gio tieu chuan: "))
giovuotchuan = max(0, sogiolam - 44)

thucluong = 44 * luonggio + giovuotchuan * luonggio *1.5

print(f"So tien thuc linh cua nhan vien: {thucluong}")