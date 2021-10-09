def multiplyx(n):
    if n==1:
        return 1
    return n * multiplyx(n-1)

a = int(input('Enter a number '))
print(sumx(a))
