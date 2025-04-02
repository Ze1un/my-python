import math
def sum_divisors(n):
    if n == 1:
        return 0
    total = 1
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt+1):
        if n % i == 0:
            total += i
            if i != n//i: #避免平方数重复加
                total += n//i
    return total
n = int(input())
if sum_divisors(n) == n:
    print("Pure")
elif sum_divisors(n) > n:
    print("Late")
else:
    print("Early")

