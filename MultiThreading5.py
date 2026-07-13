
#2+4+6+8=20
def SumEven(No):
    Sum=0

    for i in range(2,No,2):
        if(i%2==0):
            Sum=Sum+i

    print(f"Sum of Even Numbers upto {No} is :{Sum}")


#1+3+5+7+9=25
def SumOdd(No):
    Sum=0

    for i in range(1,No,2):
        if(i%2!=0):
            Sum=Sum+i

    print(f"Sum of Odd Numbers upto {No} is :{Sum}")

def main():
    SumEven(10000000)
    SumOdd(10000000)


if __name__=="__main__":
    main()