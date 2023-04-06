print("Welcome to TicTacToe :)")
def print_board(lst):
    st='''
    {}|{}|{}
    --+--+--
    {}|{}|{}
    --+--+--
    {}|{}|{}
    '''
    st=st.format(*lst)
    print(st)
lst=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
print_board(lst)