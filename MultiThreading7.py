import threading
import time

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

    start=time.perf_counter()

    t1=threading.Thread(target=SumEven,args=(100000000,))
    t2=threading.Thread(target=SumOdd,args=(100000000,))

    t1.start()
    t2.start()

    end=time.perf_counter()

    print(f"Time Taken to execute the main function is :{end-start:.4f} seconds")


if __name__=="__main__":
    main()