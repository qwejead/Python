#---------------------------------------------------|
#              LIST                 TUPLE           |  
#---------------------------------------------------|
#ORDERED        YES                 YES             |
#INDEXED        YES                 YES             |
#MUTABEL        YES                  NO             |
#HETROGENEOUS   YES                 YES             |
#---------------------------------------------------|

def main():
    Data1=[10,3.14,True,"Pune"]      #LIST
    Data2=(10,3.14,True,"Pune")      #TUPPLE

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])


if __name__=="__main__":
    main()