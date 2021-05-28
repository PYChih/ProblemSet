class LNode:
    def __init__(self, x=None):
        self.data=x
        self.next=None

def Reverse(head):
    if head==None or head.next==None or head.next.next==None:
        return
    pre = None
    cur = None
    nxt = None

    cur = head.next
    nxt = cur.next
    cur.next = None
    pre = cur
    cur = nxt
    while cur.next != None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = nxt
    cur.next = pre
    head.next = cur

if __name__=="__main__":
    i = 1
    head = LNode()
    tmp = None
    cur = head

    while i<8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    
    print("original linked list:\nhead", end="")
    cur = head.next
    while cur!=None:
        print("->{}".format(cur.data), end="")
        cur = cur.next
    print("")
    print("after reverse:\nhead", end="")
    Reverse(head)
    cur = head.next
    while cur!=None:
        print("->{}".format(cur.data), end="")
        cur = cur.next
    print("")