import math

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
    
    def __gt__(self,other):
        if(self.x > other.x):
            return True
        elif(self.x == other.x):
            if(self.y >= other.y):
                return True
            else:
                return False
        else:
            return False
List = []
path = Queue()
iterasi = 0
# heuristic adalah Manhattan distance |x1 - x2| + |y1 - y2|
def Manhattan(P1,P2):
    return (math.fabs(P1.x-P2.x)+math.fabs(P1.y-P2.y))
def AStar(start,exit):
   global iterasi
   List.append([Manhattan(start,exit),start])
   while(len(List)!=0):
       iterasi =  iterasi+1
       P = List.pop(0)
       print(P[0],P[1].toString())
       if(P[1].x  == exit.x and P[1].y == exit.y):
            print("Exit ditemukan di "+'('+str(P[1].x)+','+str(P[1].y)+')')
            return P[1]
       if(isFree(P[1].x+1,P[1].y)):
            Map[P[1].x][P[1].y] = -1
            P1 = Point(P[1].x+1,P[1].y,P[1])
            nextP = [Manhattan(P1,exit),P1]
            List.append(nextP)
       if(isFree(P[1].x-1,P[1].y)):
            Map[P[1].x][P[1].y] = -1
            P1 = Point(P[1].x-1,P[1].y,P[1])
            nextP = [Manhattan(P1,exit),P1]
            List.append(nextP)
       if(isFree(P[1].x,P[1].y+1)):
            Map[P[1].x][P[1].y] = -1
            P1 = Point(P[1].x,P[1].y+1,P[1])
            nextP = [Manhattan(P1,exit),P1]
            List.append(nextP)
       if(isFree(P[1].x,P[1].y-1)):
            Map[P[1].x][P[1].y] = -1
            P1 = Point(P[1].x,P[1].y-1,P[1])
            nextP = [Manhattan(P1,exit),P1]
            List.append(nextP)
       List.sort()
   return None
def isFree(x,y):
    if((x >= 0 and x < maxBrs) and (y>=0 and y < maxKol) and Map[x][y] == 0):
        return True
    return False 
if __name__ == "__main__":
    temp = 0
    temp2 = 0
    for x in range(0,maxBrs):
        if Map[x][0] == 0:
            temp = x
    for y in range(0,maxBrs):
        if Map[y][maxBrs-1] == 0:
            temp2 = y
    start = Point(temp,0,None)
    exit = Point(temp2,maxKol-1,None)
    print(start.toString())
    print(exit.toString())
    print(Manhattan(start,exit))
    P = AStar(start,exit)
    while (P != None):
        path.addTofront(P)
        P = P.Parent
    print(iterasi) #banyaknya loop yang digunakan
    path.Print()