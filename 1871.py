
def add(a, b):
    x = a + b
    return x


def remove_zero(x):
    lst = list(str(x))
    for i, num in enumerate(lst):
        if num == '0':
            lst.pop(i)
    return lst


def join_list(x):
    new_lst = "".join(x)
    return new_lst


def show_res(x):
    print(x)


while True:
    M,N = [int(x) for x in input().split()]
    if M == 0 and N == 0:
        break
    else:
        x = add(M,N)
        y = remove_zero(x)
        z = join_list(y)
        show_res(z)
 