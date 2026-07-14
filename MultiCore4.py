import multiprocessing
import os
import time

def SumCube(No):
    print(f"Process is Running with PID :  {os.getpid()}")
    Sum=0
    for i in range(1,No+1):
        Sum=Sum+(i**3)
    return Sum




def main():
    Ret=SumCube(5)
    Data=[10000000,20000000,30000000,40000000,50000000]
    Result=[]

    start_time=time.perf_counter()

    pobj=multiprocessing.Pool()

    Result=pobj.map(SumCube,Data)

    pobj.close()
    pobj.join()

    end_time=time.perf_counter()

    
    print(f"Result is :\n{Result}")
    print(f"Time requied  is :\n{end_time-start_time:.4f}seconds")


if __name__=="__main__":
    main()