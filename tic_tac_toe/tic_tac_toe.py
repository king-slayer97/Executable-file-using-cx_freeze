print("This is a tic tac toe game!")
l=[[0,0,0],[0,0,0],[0,0,0]]
n=9
for row in l:                                                                                             # initial status of the matrix
    print(" | ".join([str(cell) for cell in row]))
while(n>0):
    ipx=input("Player 1: Enter the cordinates of the move(X) you want to place(Eg: 1 3) :")          # player 1 turn
    ipx=ipx.split()
    c0=0
    if l[int(ipx[0])-1][int(ipx[1])-1]=="X" or l[int(ipx[0])-1][int(ipx[1])-1]=="O":
        print("Invalid move. Try another one!")
        continue
    l[int(ipx[0])-1][int(ipx[1])-1]="X"
    for row in l:
        print(" | ".join([str(cell) for cell in row]))
    if l[0][0]==l[0][1]==l[0][2]!=0 or l[1][0]==l[1][1]==l[1][2]!=0 or l[2][0]==l[2][1]==l[2][2]!=0:       # checking horizontal win
         n=0
         print("Player 1 won!!")
         break
    elif l[0][1]==l[1][1]==l[2][1]!=0 or l[0][0]==l[1][0]==l[2][0]!=0 or l[0][2]==l[1][2]==l[2][2]!=0:      #checking vertical win
         n=0
         print("Player 1 won!!")
         break
    elif l[0][0]==l[1][1]==l[2][2]!=0 or l[0][2]==l[1][1]==l[2][0]!=0:                                     #checking diagnol win
         n=0
         print("Player 1 won!!")
         break
    else:                                                                                                 #checking the count of zeroes in the matrix
        for i in range(3):
            for j in range(3):
                if l[i][j]==0:
                    c0+=1
        if c0==0:                                                                                          # if there are no zeroes, the game is a draw 
            print("It is a draw")
            break
    n=n-1    
    ipo=input("Player 2: Enter the cordinates of the move(O) you want to place(Eg: 1 1) :")             # player 2 turn
    ipo=ipo.split()
    c0=0
    if l[int(ipo[0])-1][int(ipo[1])-1]=="X" or l[int(ipo[0])-1][int(ipo[1])-1]=="O":
        print("Invalid move. Try another one!")
        continue
    l[int(ipo[0])-1][int(ipo[1])-1]="O"
    for row in l:
        print(" | ".join([str(cell) for cell in row]))
    
    if l[0][0]==l[0][1]==l[0][2]!=0 or l[1][0]==l[1][1]==l[1][2]!=0 or l[2][0]==l[2][1]==l[2][2]!=0:       # checking horizontal win
         n=0
         print("Player 2 won!!")
         break
    elif l[0][1]==l[1][1]==l[2][1]!=0 or l[0][0]==l[1][0]==l[2][0]!=0 or l[0][2]==l[1][2]==l[2][2]!=0:      #checking vertical win
         n=0
         print("Player 2 won!!")
         break
    elif l[0][0]==l[1][1]==l[2][2]!=0 or l[0][2]==l[1][1]==l[2][0]!=0:                                     #checking diagnol win
         n=0
         print("Player 2 won!!")
         break
    else:
        for i in range(3):                                                                                  #checking the count of zeroes in the matrix
            for j in range(3):
                if l[i][j]==0:
                    c0+=1
        if c0==0:
            print("It is a draw")                                                                          # if there are no zeroes, the game is a draw 
            break
    n=n-1
print("Game Over!!")                                                                                    # game over
        
