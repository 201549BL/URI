# T = number of tests
# C = consonants
# D = digits

def power_c(c):
    if c == 0:
        return 0
    else:
        return 26**c


def power_d(d):
    if d == 0:
        return 0
    else:
        return 10**d


def product(c, d):
    if c == 0 or d == 0:
        return c + d
    else:
        return c * d


T = int(input())

for num in range(T):
    C, D = [int(x) for x in input().split()]
    tc = power_c(C)
    td = power_d(D)
    print(product(tc, td))
