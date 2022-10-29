




class gamestate():
    def __init__(self):
        #the board is a 2d list each element of the list contains element containing class and colour of the objects corresponds to the naming of the png files
        self.board=[
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['  ','  ','  ','  ','  ','  ','  ','  '],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']
            ]
        self.movementlog=[]
        self.turn='white'

    def swap_turns(self):
        
        if self.turn=='white':
            self.turn='black'

        else:
            self.turn='white'
        print(self.turn)
        return self.turn

        



    def make_move(self,move):
        
        if self.board[move.startrow][move.startcol]!='  ':
            self.board[move.startrow][move.startcol]='  ' 
            self.board[move.endrow][move.endcol]=move.piecemoved
            self.movementlog.append(move)
            self.swap_turns()
            print(self.turn, 'xzy')
        
    
    def undo_move(self):
        if len(self.movementlog)!=0:
            move=self.movementlog.pop()
            self.board[move.startrow][move.startcol]=move.piecemoved
            self.board[move.endrow][move.endcol]=move.piececaptured            
            
            

    def get_valid_moves(self):
        
        print(self.turn, 'in get valid moves')
        moves=[]
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                turn=self.board[i][j][0]
                piece=self.board[i][j][1]
                
                if  self.turn=='white' or self.turn=='black':
                    if piece=='p':
                        self.get_pawn_moves(i,j,moves)
                    elif piece=='R':
                        self.get_rook_moves(i,j,moves)
                    elif piece=='N':
                       self.get_knight_moves(i,j,moves)
                    elif piece=='B':
                        self.get_bishop_moves(i,j,moves)
                    elif piece=='Q':
                       self.get_queen_moves(i,j,moves)
                    elif piece=='K':
                        self.get_king_moves(i,j,moves)
        
        return moves
       


    def get_pawn_moves(self,i,j,moves):
        if self.turn=='white': 
            if self.board[i-1][j]=='  ': #checks if the space ios empty or not
                moves.append(movement((i,j),(i-1,j), self.board))
                if i==6 and self.board[i-2][j]=="  ":
                    moves.append(movement((i,j),(i-2,j),self.board))
                if j-1>=0:
                    if self.board[i-1][j-1][0]=='b':
                        moves.append(movement((i,j),(i-1,j-1), self.board))
                if j+1<=7:
                    if self.board[i-1][j+1][0]=='b':
                        moves.append(movement((i,j),(i-1,j+1), self.board))


        else:
            print('yay')
            if self.board[i+1][j]=='  ':
                moves.append(movement((i,j),(i+1,j),self.board))
                if i==1 and self.board[i+2][j]=='  ':
                    moves.append(movement((i,j),(i+2,j),self.board))

            if j-1>=0:
                if self.board[i+1][j-1][0]=='w':
                    moves.append(movement((i,j),(i+1,j-1),self.board))

            if j+1<=len(self.board[0])-1:
                if self.board[i+1][j+1][0]=='w':
                    moves.append(movement((i,j),(i+1,j+1),self.board))
     
    
    def get_rook_moves(self,r,c,moves):
        direction=((-1,0),(0,-1),(1,0),(0,1))
        enemy='b' if self.turn=='white' else 'w'
        for d  in direction:
            for i in range(1,8):
                endrow=r+d[0]*i
                endcol=c+d[1]*i
                if 0 <= endrow<8 and 0<=endcol<8:
                    endpiece=self.board[endrow][endcol]
                    if endpiece=='  ': #empty space
                        moves.append(movement((r,c),(endrow,endcol),self.board))
                    elif endpiece[0]==enemy:
                        moves.append(movement((r,c),(endrow,endcol),self.board))
                        break
                    else:
                        break
                else:
                    break


    def get_bishop_moves(self,r,c,moves):
        direction=((-1,-1),(-1,1),(1,-1),(1,1))
        enemy='b' if self.turn=='white' else 'w'
        for d in direction:
            for i in range(1,8):
                endrow=r+d[0]*i
                endcol=c+d[1]*i
                if 0<=endrow <8 and 0<=endcol<8:
                    endpiece=self.board[endrow][endcol]
                    if endpiece=='  ':
                        moves.append(movement((r,c),(endrow,endcol),self.board))
                    elif endpiece== enemy:
                        moves.append(movement((r,c),(endrow,endcol),self.board))
                    else:
                        break
                else:
                    break
            else:
                break


    def get_knight_moves(self,r,c,moves):
        knightmoves=((-2,-2),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2), (2,-1),(2,1))
        friend='w' if self.turn=='white' else 'b'
        for m in knightmoves:
            endrow= r+m[0]
            endcol=c+m[1]
            if 0<=endrow<8 and 0<endcol<8:
                endpiece=self.board[endrow][endcol]
                if endpiece[0]!=friend:
                    moves.append(movement((r,c),(endrow,endcol),self.board))
                    

                    
    def get_queen_moves(self,r,c,moves):
        self.get_rook_moves(r,c,moves)
        self.get_bishop_moves(r,c,moves)

    

    def get_king_moves(self,r,c,moves):
        kingmoves=((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
        fren='w' if self.turn=='white' else 'b'
        for i in range(8):
            endrow=r+kingmoves[i][0]
            endcol=c+kingmoves[i][1]
            if 0<=endrow<8 and 0<=endcol<8:
                endpiece=self.board[endrow][endcol]
                if endpiece[0]!=fren:
                    moves.append(movement((r,c),(endrow,endcol),self.board))



class movement():

    rankstorows={'1':7,'2':6,'3':5,'4':4,'5':3,'6':2,'7':1,'8':0}
    rowstoranks={v:k for k,v in rankstorows.items()}
    filetocolumn={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    columntofile={v:k for k,v in filetocolumn.items()}

    def __init__(self,startsquare,endsquare,board):
        self.startrow=startsquare[0]
        self.startcol=startsquare[1]
        self.endrow=endsquare[0]
        self.endcol=endsquare[1]
        self.piecemoved=board[self.startrow][self.startcol]
        self.piececaptured=board[self.endrow][self.endcol]
        self.moveID=self.startrow*1000+self.startcol*100+self.endrow*10+self.endcol
        print(self.moveID)
        

    def __eq__(self, other):
        if isinstance(other,  movement):
            return self.moveID==other.moveID
        else:
            return False


    def chessnotation(self, row ,column):
        return self.columntofile[column]+ self.rowstoranks[row]