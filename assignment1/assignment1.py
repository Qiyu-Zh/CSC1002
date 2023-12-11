def check0(matrix):
    matrix2=matrix[:]
    x=position(matrix2)
    s=0
    matrix2.remove(' ')
    if len(matrix2)==8:
        for i in range(0,7):
            for k in range(i+1,8):
                if matrix2[i]>matrix2[k]:
                    s+=1
        if s%2==0:
            return True
        return False
    if len(matrix2)==15:
        for i in range(0,14):
            for k in range(i+1,15):
                if matrix2[i]>matrix2[k]:
                    s+=1
        if s%2==0 and x in [5,6,7,8,13,14,15,16]:
            return True
        if s%2!=0 and x in [1,2,3,4,9,10,11,12]:
            return True
        return False
def position(matrix):
    s=0
    for i in matrix:
        s+=1
        if i ==' ':
            return s
def check1(n):
    if len(n)==4:
        return True
    else:
        return False
def check2(n):
    b=[]
    for i in n:
        if i not in b:
            b.append(i)
        else:
            return False
    return True
def print_matrix(matrix):
    global choice
    s=0
    for i in matrix:
        print('%-5s'%i,end=' ')
        s+=1
        if (choice=='1' and s==3) or (choice=='2' and s==4):
            print()
            s=0
def change_fun(posi):
    global choice
    change=[]
    if (choice=='1' and posi in [1,2,4,5,7,8]) or (choice=='2' and posi in [1,2,3,5,6,7,9,10,11,13,14,15]):
        change.append(n1[0])
    if (choice=='1' and posi in [2,3,5,6,8,9]) or (choice=='2' and posi in [2,3,4,6,7,8,10,11,12,14,15,16]):
        change.append(n1[1])
    if (choice=='1' and posi in [i for i in range(1,7)]) or (choice=='2' and posi in [i for i in range(1,13)]):
        change.append(n1[2])
    if (choice=='1' and posi in [i for i in range(4,10)]) or (choice=='2' and posi in [i for i in range(5,17)]):
        change.append(n1[3])
    return change
import random
def main():
    global n1,choice
    print('Welcome to Kinley\'s sliding puzzle program!')
    print('You will choose either the 8 or 15-puzzle to play with!')
    print('And you move the tiles with the keyboard using any 4 letters')
    print('of your own choice such as letters \'l\', \'r\', \'u\', \'d\' for \nleft, right, up and down moves respectively.')
    print('initial puzzle is:')
    print('2  3  4\n8  5  6\n1  7    ' )
    print('your goal is:')
    print('1  2  3\n4  5  6\n7  8   ')
    b=1
    while b==1:
        n1=[]
        N=input('Enter 4 letters for left, right, up and down>').split()
        for i in N:
            for k in i:
                n1.append(k)
        if (check1(n1) and check2(n1))==False:
            print('Please enter four different letters!!')
        else:
            b=0
    while True:
        while True:
            choice=input('Enter 1 for 8-puzzle, 2 for 15-puzzle or q to end the game>')
            if choice in['1','2','q']:
                break
        if choice=='1':
            while True:
                matrix=random.sample([1,2,3,4,5,6,7,8,' '],9)
                if check0(matrix)==True:
                    break
            while True:
                print_matrix(matrix)
                posi=position(matrix)
                change_matrix=change_fun(posi)
                while True:
                    a=input('Enter move'+str(change_matrix)+'>>>')
                    if a in change_matrix:
                        break
                if a==n1[0]:
                    matrix[posi-1]=matrix[posi]
                    matrix[posi]=' '
                elif a==n1[1]:
                    matrix[posi-1]=matrix[posi-2]
                    matrix[posi-2]=' '
                elif a==n1[2]:
                    matrix[posi-1]=matrix[posi+2]
                    matrix[posi+2]=' '
                elif a==n1[3]:
                    matrix[posi-1]=matrix[posi-4]
                    matrix[posi-4]=' '
                b+=1
                if matrix==[1,2,3,4,5,6,7,8,' ']:
                    break
            print_matrix(matrix)
            print('Congratulations!!! Moves',b)
        if choice=='2':
            while True:
                matrix=random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' '],16)
                if check0(matrix):
                    break
            while True:
                print_matrix(matrix)
                posi=position(matrix)
                change_matrix=change_fun(posi)
                while True:
                    a=input('Enter move'+str(change_matrix)+'>>>')
                    if a in change_matrix:
                        break
                if a==n1[0]:
                    matrix[posi-1]=matrix[posi]
                    matrix[posi]=' '
                elif a==n1[1]:
                    matrix[posi-1]=matrix[posi-2]
                    matrix[posi-2]=' '
                elif a==n1[2]:
                    matrix[posi-1]=matrix[posi+3]
                    matrix[posi+3]=' '
                elif a==n1[3]:
                    matrix[posi-1]=matrix[posi-5]
                    matrix[posi-5]=' '
                b+=1
                if matrix==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']:
                    break
            print_matrix(matrix)
            print('Congratulations!!! Moves',b)
        if choice=='q':
            break
    print('game over')
main()



        
        
        





    



    
