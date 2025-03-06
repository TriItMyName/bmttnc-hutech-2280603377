def tinh_tong_so_chan(list):
    tong = 0
    for mun in list:
        if mun % 2 == 0:
            tong += mun
    return tong
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay:")
munbers = list(map(int, input_list.split(",")))

tong_chan = tinh_tong_so_chan(munbers)
print(f"Tong cac so chan trong danh sach la: {tong_chan}")