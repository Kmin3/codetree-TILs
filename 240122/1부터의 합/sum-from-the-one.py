n = int(input())
cnt = 0
for i in range(1, 101):
    cnt += i
    if n <= cnt:
        print(i)
        break