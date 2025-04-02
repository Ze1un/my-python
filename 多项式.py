MOD = 998244353
def get_numbers(n,conffcients,m,x_values):
    results = []
    for x in x_values:
        result = 0 #为了得到an
        for i in range(n,-1,-1):#采用倒序，采用Horner方法来计算多项式的值
            result = (result * x + conffcients[i]) % MOD
        results.append(result)
    print(" ".join(map(str,results)))
n = int(input())
conffcients = list(map(int, input().split()))
m = int(input())
x_values = list(map(int, input().split()))
get_numbers(n,conffcients,m,x_values)