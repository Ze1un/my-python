sentence = input('输入一句话： ')
counter = {}

for ch in sentence:
    if 'A' <=ch<='Z' or 'a' <=ch<='z':
        counter[ch] = counter.get(ch,0) + 1 #counter.get(ch,0) 得到元组中存取的次数 第一次为0
sorted_counter = sorted(counter,key = counter.get,reverse = True) #以counter.get 为依据sort
for key in sorted_counter:
    print(f'{key} 出现的次数为： {counter[key]}')