# function inside function
def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(greater,c)
print(new_greatest(10,20,30))

