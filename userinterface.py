'''
Created on 14 sep. 2018

@author: Sina
'''

class user_interface:
    occupied = [[]]
    player1 = []
    player2 = []
    values={a1:"a1", d1:"d1", g1:"g1", e1:"e1", b2:"b2", d2:"d2", f2:"f2", c3:"c3", d3:"d3", e3:"e3",
            a4:"a4", b4:"b4", c4:"c4", e4:"e4", f4:"f4", g4:"g4", c5:"c5", d5:"d5", e5:"e5", b6:"b6",            d6:"d6", f6:"f6", a7:"a7", d7:"d7", g7:"g7"}

    def print_board():
            print("",a1,".......................",d1,".......................",g1)
            print("",".","                         .","                          .")
            print("",".","                         .","                          .")
            print("",".        ",b2,".............",d2,".............",f2,"        .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .       ",c3,"....",d3,"....",e3,"       .         .")
            print("",".","        .        .         ","      .        .         .")
            print("",".","        .        .         ","      .        .         .")
            print("",a4,"......",b4,".....",c4,"            ",e4,".....",f4,"......",g4)
            print("",".","        .        .         ","      .        .         .")
            print("",".","        .        .         ","      .        .         .")
            print("",".","        .       ",c5,"....",d5,"....",e5,"       .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".","        .                .","                .         .")
            print("",".        ",b6,".............",d6,".............",f6,"        .")
            print("",".","                         .","                          .")
            print("",".","                         .","                          .")
            print ("",a7,".......................",d7,".......................",g7)
            print("Welcome to MILL! to make moves type commands in following fashion: g7 black")
            
