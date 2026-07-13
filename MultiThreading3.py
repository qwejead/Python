import threading

def Display(No):
    print(f"Inside Dispaly {No} :{threading.get_ident()}")

def main():

    print(f"Inside Main :{threading.get_ident()}")

    tobj=threading.Thread(target=Display,args=(11,))
    tobj.start()

if __name__=="__main__":
    main()