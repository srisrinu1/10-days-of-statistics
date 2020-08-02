def median(Data):
    if(len(Data)%2==1):
        return(Data[len(Data)//2])
    else:
        return(sum(Data[(len(Data)//2)-1:(len(Data)//2)+1])/2)
def Quartiles(Data):
    Q2=median(Data)
    if(N%2==1):
      Q1= median(Data[:len(Data)//2]) 
      Q3=median(Data[len(Data)//2+1:])  
    elif(N%2==0):
        Q1=median(Data[:len(Data)//2])
        Q3=median(Data[len(Data)//2:])
    return("\n".join([str(int(Q1)),str(int(Q2)),str(int(Q3))]))
N=int(input())    
Data=list(map(int,input().split()))
Data.sort()
print(Quartiles(Data))
