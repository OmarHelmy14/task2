list = []
def mults (num, length):
    x = 0
    while x < length:
        list.append(num+x*num) 
        x=x+1
    return list
print(mults(12,10))