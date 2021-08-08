n=int(input())
import sys
import os
ranks=[]
if (n>=1 and n<=1000):
    for i in range(0,n):
        
        sets=set()
        stra =input() 
        chunks = stra.split(' ')
        for m in range(0,4):
            #print(chunks[m])
            if(1<=int(chunks[m]) and int(chunks[m])<=10):
                
                sets.add(chunks[m])
            else:
                
                sys.exit()
        #print(sets)
        newar=list(sets)
        length=len(sets)
        #print(length)
        #print(len(sets))
        if((length == 2)):
            chunks.sort()
            b=chunks[0]
            if(chunks.count(b)==2):
                rank=2
            else:
                rank=1
        elif((length==3)):
            rank=2
        elif(length==4):
            rank=2
        else:
            rank=0
        ranks.append(rank)
        
    for k in ranks:
        print(k)

