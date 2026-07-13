import threading

def Display():
    print(f"Inside Dispaly :{threading.get_ident()}")

def main():

    print(f"Inside Main :{threading.get_ident()}")

    tobj=threading.Thread(target=Display)
    tobj.start()

if __name__=="__main__":
    main()