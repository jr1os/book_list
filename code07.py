INPUT_S = '''\
16,1,2,0,4,2,7,1,2,14
'''
numbers = [int(n) for n in INPUT_S.strip().split(",")]

min_value = min(
    sum(abs(n - i) for n in numbers)
    for i in range(min(numbers), max(numbers)+1)
)

print((min_value))