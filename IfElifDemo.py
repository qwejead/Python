print("Enter your Age : ")
Age=int(input())

if(Age<=5 and  Age>=0):
    print("Free")
elif(Age>5 and Age<=18):
    print(900)
elif(Age>18 and Age<=40):
    print(1200)
else:
    print(500)
