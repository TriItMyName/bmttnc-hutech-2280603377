def tao_tuple_to_list(list):
    return tuple(list)

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay:")
numbers = list(map(int, input_list.split(",")))
               
list_tuple = tao_tuple_to_list(numbers)
print("List: ", numbers)
print("List dau khi chuyen sang tuple: ", list_tuple)
