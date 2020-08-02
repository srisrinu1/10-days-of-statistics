# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
X=list(map(int,input().split()))
W=list(map(int,input().split()))
XW=list(zip(X,W))
num=sum(pair[0]*pair[1] for pair in XW)
den=sum(W)
print("{0:.1f}".format(num/den))
