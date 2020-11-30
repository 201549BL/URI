# A = old price
# B = new price
# find percentage.  x = B - A 
#                   x / A * 100 = percent increase 

def get_percentage(lst):
    old_price = lst[0]
    new_price = lst[1]
    increase = new_price - old_price
    result = increase / old_price * 100
    return result

A,B = [float(x) for x in input().split()]
lst = []
lst.append(A)
lst.append(B)
result = map(lambda x: round(x,2), lst)
print(f'{get_percentage(lst):.2f}%')