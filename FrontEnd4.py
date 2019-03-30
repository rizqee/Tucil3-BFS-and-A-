# testGui.py

import PySimpleGUI as sg
import random as rd
import sys
import pygame


def permainan(daftar): #daftar : matriks yang diambil dari input file
    pygame.init()
    win=pygame.display.set_mode((800,800))
    pygame.display.set_caption("Maze Solver Tugas Stima")

    width=17
    height=17


    run=True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run=False

        for i in range(0,len(daftar)):
            for j in range (0,len(daftar[1])):
                if ((daftar[i][j])==1):
                    pygame.draw.rect(win, (255,0,0),(j*width,i*width,width,height))
                    #pygame.display.update()
                else :
                    pygame.draw.rect(win, (255,255,255),(j*width,i*width,width,height))

        pygame.display.update()

        #pygame.draw.rect(win, (255,0,0),(10,10,width,height))



    pygame.quit()
    #print(daftar)



def readFromFile(inputFileName) :  # Ini fungsi utk membaca dari file (Salah)
    fi = open(inputFileName,"r")
    arrayOfNum = []
    for val in fi.read().split():
        arrayOfNum.append(int(val))
    fi.close()
    return(arrayOfNum)

def writeToFile(outputFileName,solut) : # Ini fungsi untuk menulis ke dalam file (Salah)
    fo = open(outputFileName,"w")
    fo.write(solut)
    fo.close()

def readFile(input): #Baru
    f = open ( input , 'r')
    l = []
    #l = [l.append(line.split() for line in f]
    #for line in f:
    #    l.append()
    with open(input) as f:
        lines = f.read().splitlines()
    l=[list(i) for i in lines]


    """
    arraylist = []
    for line in f:
        innerlist = []
        for number in line.split():
            innerlist.append(int(number))
        arraylist.append(innerlist)
    """
    #l=[line.split() in f]
    #print(l[1][1])
    #for i in range (0,len(l)):
    #    l[i][1]=l[i][1].split()
    #matrix = [[int(j) for j in range(len(l))] for i in range(m)]

    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j]=int(l[i][j])
            #l[i][j]=int(l[i][j])


    #print (l)
    #print(len(l))   #Baris
    #print(len(l[1]))    #Kolom
    return(l)





def inputNumGUI() : # fungsi gui untuk input angka dari user
    arrayOfNum = []
    #count = 0
    #while count < 4 :
    num = sg.PopupGetText('Input nama file :')
    #window = sg.Window('The Card').Layout(layout).Finalize()
    #if ((int(num) > 0) & (int(num) < 14)) :
    #arrayOfNum.append(int(num))
    #count = count+1
    #else :
        #sg.Popup('Input angka di luar range')

    return(num)
permainan(readFile(inputNumGUI()))
#readFile()
