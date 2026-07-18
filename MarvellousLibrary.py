def filterX(Task,Elements):
    Result=[]

    for no in Elements:
        Ret=Task(no)        #CheckEven(no)
        if(Ret==True):
            Result.append(no)

    return Result

def mapX(Task,Elements):    
    Result=[]

    for no in Elements:
        Ret=Task(no)                #Increment(no)
        Result.append(Ret)

    return Result

def reduceX(Task,Elements):    
    Ret=0
    for no in Elements:
        Ret=Task(Ret,no)

    return Ret