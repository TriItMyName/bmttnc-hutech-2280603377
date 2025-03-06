def dao_nguoc(list):
    return list[::-1]

input_list = input("Nhap danh sach cac so can dao nguoc, cach nhau bang dau phau: ")
numbers = list(map(int, input_list.split(",")))

list_dao_nguoc = dao_nguoc(numbers)
print("List dau khi dao nguoc: ", list_dao_nguoc)
               