n = int(input())
j = n+2
for i in range(1, n*2, 2):
    print(' ' * j, end = '')
    print('* ' * i)
    j -= 2