val = int(input("Lütfen sayıyı giriniz :"))
div = 2
if val % 2 == 0:
    if val == 2:
        print("Sayı asaldır.Böleni 2 dir.")
    else:
        print("Sayı asal değildir.")
        while val > 1:
            if val % div == 0:
                val//=div
                print("Bölenleri :",end=" ")
                print(div)
            else:
                div+=1
else:
    for i in range(3,int(val**0.5)+1,2):
        if val % i == 0:
            print("Sayı asal değildir.")
            while val > 1:
                  if val % div == 0:
                      val//=div
                      print(div,end=" ")
                  else:
                       div+=1
    else:
        print("Sayı asaldır.")
    
          
         
