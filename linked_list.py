class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertattail(self,val):
        temp=node(val)
        
        if(self.head==None):
            self.head=temp
        
        else:
            temp1=self.head
            while(temp1.next!=None):
                temp1=temp1.next
            temp1.next=temp
        self.tail=temp
    def insertathead(self,val):
        temp=node(val)
        if(self.head==None):
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
    def insertatmid(self,val,pos):
        temp=node(val)
        if(self.head==None):
            self.head=temp
            self.tail=temp
        else:
            if(pos<1):
                c.insertathead(val)
                return
            temp1=self.head
            prev=temp1
            for i in range(pos-1):
                if(prev.next==None):
                    break
                prev=prev.next
            aft=prev.next
            prev.next=temp
            temp.next=aft
    def search(self,search):
        index=0
        temp=self.head
        if(temp==None):
            return 'empty'
        else:
            while(temp):
                if(temp.val==search):
                    return 'Found at '+str(index)
                index+=1
                temp=temp.next
            if(temp==None):
                return 'Not Found'
    def removeathead(self):
        temp=self.head
        if(temp==None):
            return
        else:
            self.head=self.head.next
            del temp
    def removeattail(self):
        temp=self.head
        if(temp==None):
            return
        else:
            prev=temp
            temp=temp.next
            while(temp.next!=None):
                prev=temp
                temp=temp.next
            prev.next=None
            self.tail=prev
            del temp
    def removeatmid(self,val):
        temp=self.head
        if(temp==None):
            return
        else:
            prev=temp
            if(prev.val==val):
                return c.removeathead()
            temp=temp.next
            while(temp!=None):
                if(temp.val==val):
                    prev.next=temp.next
                    del temp
                    return
                prev=temp
                temp=temp.next
        
    def disp(self):
        temp=self.head
        while(temp):
            print(temp.val)
            temp=temp.next
if __name__ == '__main__':
    #edit below
    c=LinkedList()
    for i in range(5):
        d=i
        c.insertathead(i)
    c.disp()
    print('-----')
    c.removeatmid(0)
    c.disp()
    
    
        
