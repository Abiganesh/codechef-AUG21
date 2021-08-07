n=int(input())
ranks=[]
for i in range(0,n):
    sets=set()
    stra =input() 
    chunks = stra.split(' ')
    for m in range(0,4):
        #print(chunks[m])
        sets.add(chunks[m])
    #print(sets)
    length=len(sets)
    #print(length)
    #print(len(sets))
    if((length == 2)or(length==3)):
        rank=1
    elif(length==4):
        rank=2
    else:
        rank=0
    ranks.append(rank)
for k in ranks:
    print(k)

