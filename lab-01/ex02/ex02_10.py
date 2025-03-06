def chuoi_dao_nguoc(chuoi):
    return chuoi[::-1]
input_string = input("Nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ", chuoi_dao_nguoc(input_string))