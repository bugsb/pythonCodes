
class node:

    def __init__(self,data):
        self.data = data
        self.next = None

class linkList:
    def __init__(self):
        self.head = None
        

    def insert_at_beg( self, data ):
        newNode = node( data )
        newNode.next = self.head
        self.head = newNode

    def insert_at_end(self,data):
        newNode = node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        

    def display(self):
        if self.head == None:
            print("List khali hai baba !")
        else:
            temp = self.head
            while temp is not None:
                print("",end=" ->")
                print(temp.data,end="")
                temp = temp.next
            print("")

    def del_at_beg(self):
        if self.head == None:
            print("Kuch nahi hai delete karne ko !")
        else:
            self.head=self.head.next

    def del_at_end(self):
        if self.head == None:
            print("Kuch nahi hai delete karne ko !")
        elif self.head.next == None:
            self.head =None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None


###############################################################################

while True:
    print("\n\n\n")
    print("1.] Create List")
    print("2.] Insert At Beg")
    print("3.] Insert At Last")
    print("4.] Delete At Beg")
    print("5.] Delete At Last")
    print("6.] Display List")
    print("7.] EXIT()")

    ipt = int(input("Enter Your Choice ! "))
    if ipt == 1:
        List = linkList()
    elif ipt == 2:
        data = int(input("Enter The Data "))
        List.insert_at_beg(data)
    elif ipt == 3:
        data = int(input("Enter The Data "))
        List.insert_at_end(data)
    elif ipt == 4:
        List.del_at_beg()
    elif ipt == 5:
        List.del_at_end()
    elif ipt == 6:
        List.display()
    elif ipt == 7:
        exit()
    else:
        print("INVALID INPUT !")
