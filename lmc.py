#data = input("Nhập một ký tự: ")

# Kiểm tra đồng thời 2 điều kiện: độ dài = 1 VÀ là chữ cái
#if len(data) == 1 and data.isalpha():
    #print(f"'{data}' là một chữ cái hợp lệ.")
#else:
    #print("Không hợp lệ! Vui lòng chỉ nhập duy nhất một chữ cái.")


#x=10
#x='now a string'
#print(x)
#x=1.1+2.2
#print(isclose(x,3.3))


#a, b, c = 2, 5, 8
#print(a < b < c == 8)


#x  = 7 // 2 + 7 / 2
#print(x)

#nhập vào một số nguyên đại diện cho tháng trong năm(năm nhuận), in ra số ngày trong tháng đó
#dùng matchcase:
#thang=int(input())
nam=int(input())
match thang:
    case 1|3|5|7|8|10|12:
        print(f'thang {thang} có 31 ngày')
    case 2:
        if nam %400==0 or (nam%4 and nam%100!=0):
            print(29)
        else:
            print(28)
    case 4|6|9|11:
        print(f'thang {thang} có 30 ngày')
    case _: #truong hop con lai
        print(f'khong co thang {thang} trong nam')




#n=int(input())
#match n:
    #case n if n%2==0:
        #print('chan')
    #case _:
        #print('le')

