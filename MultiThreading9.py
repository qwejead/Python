import threading
import time

#2+4+6+8=20
def SumEven(No):
    print(f"TID of SumEven Thread is :{threading.get_ident()}")


#1+3+5+7+9=25
def SumOdd(No):
    print(f"TID of SumOdd Thread is :{threading.get_ident()}")

def main():
    print(f"TID of Main Thread is :{threading.get_ident()}")

    start=time.perf_counter()

    t1=threading.Thread(target=SumEven,args=(100000000,))
    t2=threading.Thread(target=SumOdd,args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()   

    end=time.perf_counter()

    print(f"Time Taken to execute the main function is :{end-start:.4f} seconds")


if __name__=="__main__":
    main()