
def overlap(a,b):
    l1=len(a)
    l2=len(b)
    s1=0
    s2=0
    while l1>s1:
        if(a[s1]==b[s2]):
            s1+=1
            s2+=1
        else:
            s1+=1
            s2=0       
    return a[0:s1] +b[s2:l2]
if overlap("sweden", "denmark")  == "swedenmark" :
    print("Success 1")
if overlap("honey", "milk") == "honeymilk":
    print("Success 2")
if overlap("dodge", "dodge") == "dodge":
    print("Success 3")