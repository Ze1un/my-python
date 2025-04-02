import sys
def is_contain(S,T):
    it = iter(T)
    return all(ch in it for ch in S)

lines = sys.stdin.read().splitlines()#好几行
n,m = map(int,lines[0].split())
names = lines[1:n+1]
cute_names = lines[n+1:n+1+m]
for name in names:
    score = sum(1 for word in cute_names if is_contain(word,name))
    print(score)
