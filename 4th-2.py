#CHECK WHETHER THE YEAR IS LAP YEAR OR NOT
Y=int(input("enter any year"))
if Y%4==0 and Y%100==0:
    print("not a leap year")
elif Y%100==0 and Y%400==0 :
    print("a leap year")
elif Y%4==0:
    print("a leap year")
else:
    print("not a leap year")
    
    

    
    
