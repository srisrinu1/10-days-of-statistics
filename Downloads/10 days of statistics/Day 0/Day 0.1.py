from collections import Counter
N=int(input())
Data=list(map(int,input().split()))
print("{0:.1f}".format(sum(Data)/N)) #mean
Data=sorted(Data)
#Median
if(N%2==1):
    print("{0:.1f}".format(Data[(int((N+1)/2))]))
elif(N%2==0):
    avg=0.5*(Data[int(N/2)-1]+Data[int(N/2)])
    print("{0:.1f}".format(avg))    
counts=[]
for element in Data:
    counts.append(Data.count(element))
if(max(counts)>=1):
    print(Data[counts.index(max(counts))])    
