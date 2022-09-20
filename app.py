

def printFibonnaci(maxNbrs):
    sec=0
    last=1
    for i in range(0,maxNbrs):
        if(i<2):
            print(i)
            continue
        temp=sec+last
        last=sec
        sec=temp
        print(temp)

nbrs2print=input("Choose how many numbers of the fibonacci sequence you wanna print: ")
printFibonnaci(int(nbrs2print))



