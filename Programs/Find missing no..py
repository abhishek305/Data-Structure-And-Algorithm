def findmiss(a):
        n=len(a)
        total=(n+1)*(n+2)/2
        suma=sum(a)
        return total-suma

a=[int(x) for x in input().split()]
miss=findmiss(a)
print(int(miss))

