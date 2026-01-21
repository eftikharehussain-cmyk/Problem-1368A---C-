# Problem-1368A---C-
for _ in range(int(input())):
    a, b, n = map(int, input().split())
    count = 0
    while a <= n and b <= n:
        if a < b:
            a += b
            count += 1
        else:
            b += a
            count += 1
    print(count)
