

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
    return(Q1,Q2,Q3)
N=int(input())    
X=list(map(int,input().split()))
f=list(map(int,input().split()))
s=[]
for i in range(len(X)):
    s.extend([X[i]]*f[i])
s.sort()    
Q1,Q2,Q3=Quartiles(s)
print("{:.1f}".format(Q3-Q1))
