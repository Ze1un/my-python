import sys
def choice(options):
    length = [len(opt[2:]) for opt in options]
    min_length = min(length)
    max_length = max(length)
    if length.count(min_length) == 1:
        return options[length.index(min_length)][0]
    if length.count(max_length) == 1:
        return options[length.index(max_length)][0]
    return "C"
lines = sys.stdin.read().splitlines()
T = int(lines[0])
result = []
for i in range(T):
    questions = lines[1+i*4:1+(i+1)*4]
    result.append(choice(questions))
print("\n".join(result))