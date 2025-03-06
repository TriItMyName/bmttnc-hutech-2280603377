def den_so_lan_xuat_hien(list):
    count_dict = {}
    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhap danh sach cac phan tu, cach nhau bang dau phap: ")

word_list = input_string.split()

so_lan_xuat_hien = den_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu: ", so_lan_xuat_hien)
        