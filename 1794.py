# LA, LB = min wash, max wash
# SA, SB = min dryer, max dryer

N = int(input())

LA, LB = [int(x) for x in input().split()]
SA, SB = [int(x) for x in input().split()]

if N >= LA and N <= LB and N >= SA and N <= SB:
    print('possivel')
else:
    print('impossivel')

