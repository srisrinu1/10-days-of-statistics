# Enter your code here. Read input from STDIN. Print output to STDOUT

def standardDeviation(Data):

    sd=(sum((x-Mean)**2 for x in Data)/N)**0.5
    return("{0:.1f}".format(sd))

if __name__=="__main__":
    N=int(input())
    Data=list(map(int,input().split()))
    Mean=sum(Data)/N
    print(standardDeviation(Data))
