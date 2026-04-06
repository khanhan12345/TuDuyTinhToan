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
#nam=int(input())
#match thang:
   ## case 1|3|5|7|8|10|12:
 #       print(f'thang {thang} có 31 ngày')
  #  case 2:
 #   #    if nam %400==0 or (nam%4 and nam%100!=0):
#print(29)
    #    else:
      #      print(28)
   # case 4|6|9|11:
#print(f'thang {thang} có 30 ngày')
   ##  print(f'khong co thang {thang} trong nam')




#n=int(input())
#match n:
    #case n if n%2==0:
        #print('chan')
    #case _:
        #print('le')


#print(list(range(10)))



#while True:
##n=int(input())
   # if n<=0:
    #    continue
    #    print('hello')
   # else:
   #     break
#for i in range(1,10):
    #print(i, end=' ')
   # if i%7==0:
       # break
#else:
   # print('\nxong')


 ## print(i, end=' ')
#else:
  #print('\nxong')


#nhập 1 số nguyên đến khi đc 1 số nguyên dương thì thôi, kiểm tra xem nó có phải số nguyên tố hay không
#=-10
#while n<=0:
    #n=int(input())
#print(n)
    
#dem so uoc->neu so uoc bang 2 thi no la so nguyen to
#
#count=0
#n=int(input())
##for i in range(1,n+1):
   # if n%i==0:
   #     count=count+1
#if count==2:
   # print('so nguyen to')

#cachkhac, tính tổng các số nguyên tố/đoạn a,b

#n=int(input())
#count=0
###for i in range(2,int(n**0.5)+1):
    #if n%i==0:
       # print('khong la so nguyen to')
       # break
#else:
   # print('so nguyen to')


#nhập vào a,b cho đến khi a, b nguyên dương và a<b thì thôi.tính tổng ccác số nguyên tố trên đoạn a.b
#=int(input())
#b=int(input())
#tong=0
#while a<=0:
   # a=int(input())
   # b=int(input())
   # while a>=b:
       # a=int(input())
      #  b=int(input())
       # if a<b:
           # for i in range(2,int(b**0.5)+1):
             #   for n in range(a,b+1):
                 #   if n%i==0:
                     #   tong=tong+i
#print(tong)

về nhà: nhập một số nguyên n (n<=1000). in ra tất cả các số nguyên tố nhỏ hơn or bằng n(dùng sàng eratosthenes)
nhập một số nguyên n, in ra dãy số nguyên  liên tiếp dài nhất không chứa số nguyên tố nào
(dãy nào tìm thấy đầu tiên thì in ra)

