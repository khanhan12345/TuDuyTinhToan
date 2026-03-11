data = input("Nhập một ký tự: ")

# Kiểm tra đồng thời 2 điều kiện: độ dài = 1 VÀ là chữ cái
if len(data) == 1 and data.isalpha():
    print(f"'{data}' là một chữ cái hợp lệ.")
else:
    print("Không hợp lệ! Vui lòng chỉ nhập duy nhất một chữ cái.")