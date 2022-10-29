'''the main file containing pygame and all the inputs arte taken here'''
from chess import chess_engine
import pygame   

width=height=480
dimension=8 #the number of rows and columns here 8 because a chess board has 8 rows and 8 columns  
square_size=height//dimension

maxfps=30
images={}

def chess_pieces(): #THIS FUNCTION IS USED FOR LOADING IMAGES OF CHESS PIECESON THE BOARD
    global images
    pieces=['wR','wN','wB','wQ','wK','wp','bR','bN','bB','bQ','bK','bp']
    for i in pieces:
        images[i]=pygame.transform.scale(pygame.image.load("chess_pieces/"+i+".png"),(square_size,square_size))
    

def main():
    #main  of the game here only all the stuff take place
    
    pygame.init()
    screen=pygame.display.set_mode((width,height))
    screen.fill(pygame.Color("white"))
    running=True
    clock=pygame.time.Clock()
    chess_pieces() #this functions is used to create chess pieces and link then to the image file of the respective piece stored locally
    gs=chess_engine.gamestate()    
    drawState(screen,gs)
    running=True
    sqsel=() #keeps track of the selected square
    playerclicks=[] #keeps tracks of the cklicks like first square selected and the second square to be selected
    valid_moves=gs.get_valid_moves()
    move_made=False    
    while running: #event loop

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        
            elif event.type==pygame.MOUSEBUTTONDOWN:
                location=pygame.mouse.get_pos()
                column=location[0]//square_size
                row = location[1]//square_size

                if sqsel==(row,column): #this block used to unselect if same square are selected twice
                    sqsel=()
                    playerclicks=[]                    

                else:
                    sqsel=(row,column)
                    playerclicks.append(sqsel) #append the move to player clicks (keeps log of movements)

                if len(playerclicks)==2: #to move the piece to the other place
                   
                    move=chess_engine.movement(playerclicks[0],playerclicks[1],gs.board)
                    if move in valid_moves:
                        gs.make_move(move)                       
                        sqsel=()                        
                        playerclicks=[]                    
                    else:
                        playerclicks=[sqsel]
                    
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_z:
                    gs.undo_move()
                    move_made=True 

        drawState(screen,gs)
        clock.tick(maxfps)
        pygame.display.flip()
     
def drawState(screen,gs): #method to draw sqares and place pieces on the screen consists of drawpieces and drawboard
    drawBoard(screen)
    drawPieces(screen,gs)


def drawBoard(screen): #just to draw the squares 
    colours=[pygame.Color('white'),pygame.Color('grey')]
    for i in range(dimension):
        for j in range(dimension):
            colour=colours[(i+j)%2]        
            pygame.draw.rect(screen,colour,pygame.Rect(j*square_size,i*square_size,square_size,square_size))




def drawPieces(screen,gs):   
    for i in range(8):
        for j in range(8):
            piece=gs.board[i][j]
            if piece!='  ':
                screen.blit(images[piece],pygame.Rect(j*square_size,i*square_size,square_size,square_size))


main()

