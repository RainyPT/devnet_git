import json
def printFibonnaci(maxNbrs):
    listerinos=[]
    sec=0
    last=1
    for i in range(0,maxNbrs):
        if(i<2):
            listerinos.append(i)
            continue
        temp=sec+last
        last=sec
        sec=temp
        listerinos.append(temp)
    return listerinos

nbrs2print=input("Choose how many numbers of the fibonacci sequence you wanna print: ")
with open("data.json","w") as file:
    json.dump("{fibosequence:"+str(printFibonnaci(int(nbrs2print)))+"}",file)

