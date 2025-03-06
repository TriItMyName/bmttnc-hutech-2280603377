print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)

print("Cac dong da nhap khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())