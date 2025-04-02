def get_the_closed(N,Nums,M):
    for _ in range(M):
        x = int(input())
        min_diff = float('inf')
        closed_num = float('inf')
        for num in Nums:
            diff = abs(num - x)
            if diff < min_diff:
                min_diff = diff
                closed_num = num
            elif diff == min_diff and num < closed_num:
                closed_num = num
        print(closed_num)
N = int(input())
Nums = list(map(int,input().split()))
M = int(input())
get_the_closed(N,Nums,M)

