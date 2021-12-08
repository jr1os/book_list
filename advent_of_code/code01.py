INPUT_S = '''\
199
200
208
210
200
207
240
267
260
263
'''

numbers = [int(line) for line in INPUT_S.splitlines()]

prev = numbers[0]
count = 0

#for i in numbers[1:]:
    #if i > prev:
        #count += 1
    #prev = i

#print(count)

#for i in range(1, len(numbers)):
    #if numbers[i] > numbers[i - 1]:
        #count += 1
    
count = sum(
    numbers[i] > numbers[i - 1] for i in range(1, len(numbers))
)
print(f"part 1: {count}")
    
count = sum(
    numbers[i] > numbers[i - 3] for i in range(3, len(numbers))
)
print(f"part 2: {count}")