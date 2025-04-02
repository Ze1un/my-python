import sys
import bisect
def get_the_closed(N,Nums,M):
    Nums.sort()
    for x in queries:
        idx = bisect.bisect_left(Nums,x)#返回二分查找 离x最近的索引位置 从左到右
        candidates = []
        if idx < N:
            candidates.append(Nums[idx]) #x 右侧或本身
        if idx > 0:
            candidates.append(Nums[idx-1]) #x 左侧
        closed_value = min(candidates,key = lambda num:(abs(x-num),num)) #以diff 和 num 排序
        print(closed_value)
input_data = sys.stdin.readline().split()
N = int(input_data[0])
Nums = list(map(int,input_data[1:N+1]))
M = int(input_data[N+1])
queries = list(map(int,input_data[N+2:]))
get_the_closed(N,Nums,M)
