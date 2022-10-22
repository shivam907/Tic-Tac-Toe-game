from operator import indexOf


def replacer(s, n, i):                                                                                             #it fits the value given by user of X/0 in to the structure of TicTacToe
    if i < 0:
        return n + s
    if i > len(s):
        return s + n
    else:
        if(i<=13):
            return s[:i] + n + s[i+ 1:]
        return s[:i+1] + n + s[i+ 2:]

def input_positions(s, c):                                                                                         #it takes Input from users of the positions where they want to move there turn and checks that is't that space occupied and 
    print("Enter the Position where you want to Move {} ".format(s))
    ba = input()
    if ba.isdigit():
        b=int(ba)
        l.append(b)
        if l.count(b)>=2:
            print("Sorry This Place is Already Occupied Try Another ")
            return 0
        else:
            h=replacer(c, s, pos[b-1])
            return h
    else:
        print("You have Not Entered a Digit Please Enter Again ")
        return 0


a='''___|___|___|___
___|___|___|___
___|___|___|___
   |   |   |   '''
n=a

n1='''_1_|_2_|_3_|_4_
_5_|_6_|_7_|_8_
_9_|10_|11_|12_
13 |14 |15 |16 '''



print("Enter Position Where You want to Put your Move  \n{} ".format(a))
print("Positions are defined as \n{}".format(n1))

print()
print()
print(n1[37])

pos=[1,5,9,13,16,20,24,28,32,36,40,44,48,52,56,60]

l=[]
i=1
b=True


while b:                                                                        #while loop calls the input function and prints the current position of the TicTacToe Structure  and also check for a winner simultaneously if someone has won then the loop breaks
    if b:
        if i%2!=0 and b :
            s=input_positions("X", a)
            if s!=0:
                a=s
                print(s)
        else:
            s=input_positions("O", a)
            if s!=0:
                a=s
                print(s)
        if s!=0:
            i+=1
            if i==len(pos)+1:
                b=False
        
        if s!=0:
            if s[1]==s[5]==s[9]==s[13]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[1]==s[5]==s[9]==s[13]=="O":
                print("O is the Winner")
                b=False
                break
            if s[17]==s[21]==s[25]==s[29]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[17]==s[21]==s[25]==s[29]=="O":
                print("O is the Winner")
                b=False
                break
            if s[33]==s[37]==s[41]==s[45]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[33]==s[37]==s[41]==s[45]=="O":
                print("O is the Winner")
                b=False
                break
            if s[49]==s[53]==s[57]==s[61]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[49]==s[53]==s[57]==s[61]=="O":
                print("O is the Winner")
                b=False
                break
            if s[1]==s[17]==s[33]==s[49]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[1]==s[17]==s[33]==s[49]=="O":
                print("O is the Winner")
                b=False
                break
            if s[5]==s[21]==s[37]==s[53]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[5]==s[21]==s[37]==s[53]=="O":
                print("O is the Winner")
                b=False
                break
            if s[9]==s[25]==s[41]==s[57]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[9]==s[25]==s[41]==s[57]=="O":
                print("O is the Winner")
                b=False
                break
            if s[13]==s[29]==s[45]==s[61]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[13]==s[29]==s[45]==s[61]=="O":
                print("O is the Winner")
                b=False
                break


            if s[1]==s[21]==s[41]==s[61]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[1]==s[21]==s[41]==s[61]=="O":
                print("O is the Winner")
                b=False
                break
            if s[13]==s[25]==s[37]==s[49]=="X":
                print("X is the Winner")
                b=False
                break
            elif s[13]==s[25]==s[37]==s[49]=="O":
                print("O is the Winner")
                b=False
                break