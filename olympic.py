n=int(input())

ranking=[]
for i in range(0,n):
    total=0
    total1=0
    stra =input() 
    chunks = stra.split(' ')
    for j in range(0,3):
        total=total+int(chunks[j])
        print(chunks[j])
    for k in range(3,6):
        total1=total1+int(chunks[k])
    if(total>total1):
        rank=1
    else:
        rank=2
    ranking.append(rank)
    print(total)
    print(total1)
        
for m in ranking:
    print(m)
print(type(chunks))