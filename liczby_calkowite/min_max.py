def min_zbioru(zbior):
    min = zbior[0]
    for i in zbior:
        if min > i: min = i
    return min
def max_zbioru(zbior):
    max = zbior[0]
    for i in zbior:
        if max < i: max = i
    return max

zbior = [5,2,8,2,89,1,-1,65]
print("wartość najmniejsza zbioru: ", min_zbioru(zbior))
print("wartość największa zbioru: ", max_zbioru(zbior))
