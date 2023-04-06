word='python'
target = '__th_n'
n=5


print('welcome to hamgman')
print(target)
p=False
y=False
o=False

while n>0:

    print(f"Guess the missing letters\nAttempts left:{n}")
    guess=input()

    if guess == 'p':
        p=True
    elif guess=='y':
        y=True
    elif guess=='o':
        o=True
    
    else:
        n -= 1

    if y and o and p:
        print('python')
        print("You Win")
        break 

    elif y and o:
        print('_yhton')
    elif y and p:
        print('pyht_n')
    elif p and o:
        print('p_hton')
    
    elif p:
        print('p_ht_n')
    elif y:
        print('_yht_n')
    elif o:
        print('__thon')
    
    else:
        print("You lost \n Good Bye")
        