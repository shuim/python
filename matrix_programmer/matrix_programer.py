count = 0

def mul(p,q,count):
    if p*q==1:
        count+=1
        if count<=10:
            mul(p,q,count)
            print(count)
mul(1,1,count)
