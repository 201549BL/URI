def tea_test():
    T = int(input())
    answers = [int(x) for x in input().split()]
    counter = 0
    for answer in answers:
        if answer == T:
            counter +=1
    return counter

print(tea_test())
