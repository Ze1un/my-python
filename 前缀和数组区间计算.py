import sys

n,k = map(int,sys.stdin.readline().split())
w = list(map(int,sys.stdin.readline().split()))
output = []
prefix = [0] * (n+1)
for i in range(1,n+1):
    prefix[i] = prefix[i-1] + w[i-1]
for _ in range(k):
    l,r = map(int,sys.stdin.readline().split())
    output.append(prefix[r]-prefix[l-1])
sys.stdout.write("\n".join(output)+'\n')