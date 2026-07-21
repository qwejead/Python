no=11 

def Display():
    global no               #new word
    no=21
    print("From Display :",no)


print("Before :",no)
Display()
print("After :",no)