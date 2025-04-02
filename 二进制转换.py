def binary_addition(A, B):
    binary_A = bin(A)[2:]
    binary_B = bin(B)[2:]

    max_len = max(len(binary_A), len(binary_B))
    binary_A = binary_A.zfill(max_len)
    binary_B = binary_B.zfill(max_len)

    result = ''
    for a, b in zip(binary_A, binary_B):
        sum_bits = int(a) + int(b)
        result += str(sum_bits)

    return int(result)
input_values = input().split()
A = int(input_values[0])
B = int(input_values[1])
print(binary_addition(A, B))