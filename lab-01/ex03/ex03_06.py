def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key_to_delete = 'c'

result = xoa_phan_tu(my_dict, key_to_delete)

if result:
    print(f"Da xoa phan tu co key la {key_to_delete}")
    print("Dictionary sau khi xoa:", my_dict)
else:
    print(f"Phan tu co key la {key_to_delete} khong ton tai trong dictionary")