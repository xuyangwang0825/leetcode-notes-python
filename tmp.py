def getNthFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (getNthFib(n-1) + getNthFib(n-2))

print(getNthFib(6))