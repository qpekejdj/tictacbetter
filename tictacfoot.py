Rows = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
    ]
mark = "     |     |"
boop = "- - - - - - - - -"
def drawgame():
    print(mark)
    print(f"  {Rows[0][0]}  |  {Rows[0][1]}  |  {Rows[0][2]}  ")
    print(mark)
    print(boop)
    print(mark)
    print(f"  {Rows[1][0]}  |  {Rows[1][1]}  |  {Rows[1][2]}  ")
    print(mark)
    print(boop)
    print(mark)
    print(f"  {Rows[2][0]}  |  {Rows[2][1]}  |  {Rows[2][2]}  ")
    print(mark)
    print()

def place(pie):
    a = 0
    Placed = False
    while Placed == False:
        while a < 1 or a > 9:
            try:
                a = int(input('Player '+pie+': where to place? '))
            except:
                a = 0
        
        if Rows[(a-1)//3][(a-1)%3] != 'X' or 'O':
            Rows[(a-1)//3][(a-1)%3] = pie
            Placed = True
        a = 0

def win(winner):
    print(winner, 'has won')
    print()
    print('Congrats')
    exit()

def wincheck(who):
    if Rows[0][2] == who and Rows[1][1] == who and Rows[2][0] == who:
        win(who)
    hoof, howf,gwog = 0,0,0
    for gaag in range(3):
        if Rows[gaag][gaag] == who:
                gwog += 1
        for goog in range(3):
            if Rows[gaag][goog] == who:
                hoof += 1
            if Rows[goog][gaag] == who:
                howf += 1
        if hoof == 3 or howf == 3:
            win(who)
        else:
            hoof, howf = 0,0
    if  gwog == 3:
        win(who)

    Tied = True
    for boobs in Rows:
        for bubs in boobs:
            if bubs in '123456789':
                Tied = False  
    
    if Tied == True:
        print('How sad it\'s a tie')
        print()
        print('Try to win next time ok?')
        exit()
def play(game):
    place(game)
    drawgame()
    wincheck(game)

drawgame()

while True:



    play('X')

    play('O')





