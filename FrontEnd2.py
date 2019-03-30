# testGui.py

import PySimpleGUI as sg
import random as rd
import sys
import pygame


def permainan(daftar): #daftar : matriks yang diambil dari input file
    pygame.init()
    win=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Maze Solver Tugas Stima")

    width=10
    height=10


    run=True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run=False

        for i in range(0,len(daftar)):
            for j in range (0,len(daftar[1])):
                if ((daftar[i][j])==1):
                    pygame.draw.rect(win, (255,0,0),(j*10,i*10,width,height))
                    #pygame.display.update()

        pygame.draw.rect(win, (255,0,0),(10,10,width,height))



    pygame.quit()




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
    l = [line.split() for line in f]
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j]=int(l[i][j])
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
