#program dapat melakukan BFS pada matriks
Map = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1],
    [1,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,0],
    [1,1,1,1,1,1,1,1,1,1,1]
]
# Map merupakan contoh Maze
maxBrs = len(Map)
maxKol = len(Map[0])
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isMember(self,data):
        temp = self.head
        found = False
        while(temp != None and found == False):
            if(temp.data.x == data.x and temp.data.y == data.y):
                found = True
            else:
                temp = temp.next
        return found
    def addTofront(self,data):
        if(self.tail is None):
            self.head = Node(data)
            self.tail = self.head
        elif(self.isMember(data)):
            return
        else:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
    def add(self,data):
        if(self.tail is None):
            self.head = Node(data)
            self.tail = self.head
        elif(self.isMember(data)):
            return
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    def remove(self):
        if(self.head is None):
            return None
        elif(self.head == self.tail):
            temp = self.head.data
            self.head = None
            self.tail = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp
    def isEmpty(self):
        if(self.head == None ):
            return True
        return False
    def Print(self):
        if(self.isEmpty()):
            print("The queue is Empty")
        else:
            temp = self.head
            while(temp.next != None):
                print('('+str(temp.data.x)+','+str(temp.data.y)+')',end = " -> ")
                temp = temp.next
            print('('+str(temp.data.x)+','+str(temp.data.y)+')')

class Point:
    def __init__(self,x,y,Parent=None):
        self.x = x
        self.y = y
        self.Parent = Parent
    def getParent(self):
        return self.Parent
    def toString(self):
        return("x = "+str(self.x)+" y = "+str(self.y))
q = Queue() #queue untuk melakukan BFS
path = Queue() #path yang dilalui untuk mencapai exit
iterasi = 0
def BFSPath(x,y):
    global iterasi
    q.add(Point(x,y,None))
    while(q.isEmpty() == False):
        iterasi += 1
        P = q.remove()
        if(P.y == maxKol-1 and Map[P.x][P.y] == 0):
            print("Exit ditemukan di "+'('+str(P.x)+','+str(P.y)+')')
            return P
        if(isFree(P.x+1,P.y)):
            Map[P.x][P.y] = -1
            nextP = Point(P.x+1,P.y,P)
            q.add(nextP)
        if(isFree(P.x-1,P.y)):
            Map[P.x][P.y] = -1
            nextP = Point(P.x-1,P.y,P)
            q.add(nextP)
        if(isFree(P.x,P.y+1)):
            Map[P.x][P.y] = -1
            nextP = Point(P.x,P.y+1,P)
            q.add(nextP)
        if(isFree(P.x,P.y-1)):
            Map[P.x][P.y] = -1
            nextP = Point(P.x,P.y-1,P)
            q.add(nextP)

    return None
def isFree(x,y):
    if((x >= 0 and x < maxBrs) and (y>=0 and y < maxKol) and Map[x][y] == 0):
        return True
    return False
if __name__ == "__main__":
    temp = 0
    for x in range(0,maxBrs):
        if Map[x][0] == 0:
            temp = x
    P = BFSPath(temp,0)
    temp1 = Queue()
    while P is not None:
        path.addTofront(P)
        P = P.Parent
    print(iterasi)#banyaknya loop yang digunakan
    path.Print()