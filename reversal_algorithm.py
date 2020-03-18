a=[1,2,3,4,5,6,7]
b=a[:]
d=2

def reverse(a,d,n):
    c=0
    for i in range(d,n):
        if((n-c)>i):
            a[i],a[n-c-1]=a[n-c-1],a[i]
        c+=1
    print(a)
print('left rotation')
reverse(a,0,d)
reverse(a,d,len(a))
reverse(a,0,len(a))
print('right rotation')
a=b[:]
reverse(a,len(a)-d,len(a))
reverse(a,0,len(a)-d)
reverse(a,0,len(a))
