def value_cauculate(n,list):
    arr = []
    total_count = 0
    for value in list:
        cauculate = bin(abs(value))[2:]
        one_count = cauculate.count('1')
        zero_count = cauculate.count('0')
        if one_count > zero_count:
            total_count += 1
        else:
            total_count -= 1
    return total_count
n = int(input())
list = list(map(int,input().split()))
print(value_cauculate(n,list))


