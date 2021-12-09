INPUT_S = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2
'''
position = depth = aim = 0

#for line in INPUT_S.splitlines():
    #command, n_s = line.split()
    #n = int(n_s)

    #if command == 'up':
        #depth -= n
    #elif command == 'down':
        #depth += n
    #elif command == 'forward':
        #position += n
    #else:
        #raise AssertionError(f"Unreacheble {command} {n}") 



for line in INPUT_S.splitlines():
    command, n_s = line.split()
    n = int(n_s)

    if command == 'up':
        aim -= n
    elif command == 'down':
        aim += n
    elif command == 'forward':
        position += n
        depth += aim * n
    else:
        raise AssertionError(f"Unreacheble {command} {n}") 


print(position * depth)