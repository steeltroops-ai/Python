import random

print("Welcome to TicTacToe :)")
def print_board(lst):
    st='''
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    '''
    st=st.format(*lst)
    print(st)

turn=['X','0']
turn=random.choice(turn)
lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
while 1:
    print_board(lst)
    loc=int(input(f'This is your turn {turn}\nEnter move location'))
    if lst[loc]==' ':
        lst[loc]=turn
    else:
        print('Location already used,Try Next')
        continue
    #logic
    if lst[0]==lst[3]==lst[6] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[1]==lst[4]==lst[7] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[2]==lst[5]==lst[8] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[0]==lst[4]==lst[8] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[6]==lst[4]==lst[2] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[0]==lst[1]==lst[2] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[3]==lst[4]==lst[5] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    elif lst[6]==lst[7]==lst[8] != ' ':
        print_board(lst)
        print(f"{turn} WON")
        break
    if turn=='X':
        turn='0'
    else:
        turn='X'