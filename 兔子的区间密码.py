def max_xor_get(L,R): #得到区间的最大异或值
    m = 1
    xor = L^R #得到不同位
    while xor:
        m <<= 1
        xor >>= 1
    return m-1
def max_xor2(L,R):
    return 1<<(L^R.bit_length()) - 1 #1 << n 生成 长度为n的最高位为1，其余为0，bit_length()返回最高位
def max_xor3(L,R):
    max_xor = 0
    for a in range(L,R+1):
        for b in range(a,R+1):
            max_xor = max(max_xor,a^b)
    return max_xor
T = int(input())
for _ in range(T):
    L,R = map(int, input().split())
    print(max_xor_get(L,R))