n=input()
k=int(input())
f=len(n)-k
m=n.index(min(n[:f]))
g=n[m:]
k=k-m
g=list(g)
for i in range(k):
    g.remove(max(g))
print("".join(g))
