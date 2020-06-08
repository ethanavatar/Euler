# https://projecteuler.net/problem=5

i = 0
while 1:
    i += 1
    for j in range(1, 20):
        if i % j == 0:
            continue
        else:
            break
    else:
        print(i)
        break