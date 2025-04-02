def get_new_char(n,s):
    result = []
    for i in range(n):
        shift = i + 1
        if (i+1)%2 == 1:
            new_char = chr((ord(s[i])-ord('a')+shift)%26+ord('a'))
            result.append(new_char)
        else:
            new_char = chr((ord(s[i])-ord('a')-shift)%26+ord('a'))
            result.append(new_char)
    print(''.join(result))
n = int(input())
s = input().strip()
get_new_char(n,s)

