#array rotation
def lef_arr_rot(k=0,arr1=[]):
    arr=arr1.copy()
    while(k):
        arr.append(arr.pop(0))
        k-=1
    print('Left Rotation',arr)
def right_arr_rot(k=0,arr=[]):
    arr=arr1.copy()
    while(k):
        arr=[arr.pop(-1)]+arr
        
        k-=1
    print('Right Rotation',arr)

if __name__ =='__main__':
        k=int(input('Enter rotation times: '))
        arr=[]
        n=0
        
        while(True):
            try:
                c=input('Enter array element '+str(n+1)+'(Enter to Break)'+':')
            except:
                break
            arr.append(int(c))
            n+=1
        if(k>=n):
            k=k%n
        print('Original array',arr)
        lef_arr_rot(k,arr)
        right_arr_rot(k,arr)
        
