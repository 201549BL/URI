T = int(input())

triple = ['a', 'e', 'i', 'o', 's']

for num in range(T):
    triple_acc = 1
    double_acc = 1
    S = input().lower()
    for letter in S:
        if letter in triple:
            if triple_acc == 1:
                triple_acc += 2
            else:
                triple_acc = triple_acc * 3
        else:
            if double_acc == 1:
                double_acc += 1
            else:
                double_acc = double_acc * 2
    result = triple_acc * double_acc
    print(result)
