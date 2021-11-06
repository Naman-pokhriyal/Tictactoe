import random
import tkinter as tk
import tkinter.font as tkfont

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
game = 1
def Win(sym):
    i = 0
    while(i<9):        
        if(board[i]==sym and board[i+1]==sym and board[i+2]==sym):
            return True
        i = i+3
    i =0
    while(i<3):        
        if(board[i]==sym and board[i+3]==sym and board[i+6]==sym):
            return True
        i = i+1
    if((board[0]==sym and board[4]==sym and board[8]==sym) or (board[2]==sym and board[4]==sym and board[6]==sym)):
        return True
    return False

def Layout(move):
    move = move+1
    if(move == 1):
        Label1['text'] = 'O'
        Label1['fg'] = 'black'
    elif(move == 2):
        Label2['text'] = 'O'
        Label2['fg'] = 'black'
    elif(move == 3):
        Label3['text'] = 'O'
        Label3['fg'] = 'black'
    elif(move == 4):
        Label4['text'] = 'O'
        Label4['fg'] = 'black'
    elif(move == 5):
        Label5['text'] = 'O'
        Label5['fg'] = 'black'
    elif(move == 6):
        Label6['text'] = 'O'
        Label6['fg'] = 'black'
    elif(move == 7):
        Label7['text'] = 'O'
        Label7['fg'] = 'black'
    elif(move == 8):
        Label8['text'] = 'O'
        Label8['fg'] = 'black'
    elif(move == 9):
        Label9['text'] = 'O'
        Label9['fg'] = 'black'

def Comp():
    possible = []
    for move in range(0,9):
        if(board[move]==' '):
            possible.append(move)
    if(possible == []):
        move = -1
        return move

    sym = ['O','X']
    for x in sym:
        for move in possible:
            board[move] = x
            if(Win(x)):
                board[move] = ' '
                return move
            board[move] = ' '
    move = random.choice(possible)
    return move

def ResetAll():
    global board, game
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    game = 1
    Label1['text'] = '1'
    Label1['fg'] = '#f0f0f0'
    Label2['text'] = '2'
    Label2['fg'] = '#f0f0f0'
    Label3['text'] = '3'
    Label3['fg'] = '#f0f0f0'
    Label4['text'] = '4'
    Label4['fg'] = '#f0f0f0'
    Label5['text'] = '5'
    Label5['fg'] = '#f0f0f0'
    Label6['text'] = '6'
    Label6['fg'] = '#f0f0f0'
    Label7['text'] = '7'
    Label7['fg'] = '#f0f0f0'
    Label8['text'] = '8'
    Label8['fg'] = '#f0f0f0'
    Label9['text'] = '9'
    Label9['fg'] = '#f0f0f0'
    Result['text'] = ""
    Reset.place_forget()
    

class Obj:
    def Dim(self, event):
        global game
        try:
            i = int(event.widget['text'])-1
        except:
            return
        if(board[i]==' ' and game == 1):
            event.widget['text'] = 'X'
            event.widget['fg'] = 'black'
            board[i] = 'X'
        
            if(Win('X')):
               Result['text'] = "YOU WIN !!!"
               game = 0
               Reset.place(relx = 0.85, rely =0.45)
               return
            move = Comp()
            if(move == -1):
                Result['text'] = "DRAW !!!"
                game = 0
                Reset.place(relx = 0.85, rely =0.45)
                return
            board[move] = 'O'
            Layout(move)
            if(Win('O')):
                Result['text'] = "BOT WINS !!!"
                game = 0
                Reset.place(relx = 0.85, rely =0.45)
                return
    

root = tk.Tk()
root.title("")
photo = tk.PhotoImage(file = "t.png")
root.iconphoto(False, photo)
root.geometry("200x200")
root.minsize(width=200, height=200)
root.maxsize(width=200, height=200)

myFont1 = tkfont.Font(size = 16)
myFont2 = tkfont.Font(size = 12)

Tittle = tk.Label(text = "Tic - Tac - Toe", width=200, pady = 10, font = myFont1)
Canvas1 =tk.Canvas(bg = 'blue')
Label2 = tk.Label(Canvas1, text = '2', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label1 = tk.Label(Canvas1, text = '1', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label3 = tk.Label(Canvas1, text = '3', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label4 = tk.Label(Canvas1, text = '4', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label5 = tk.Label(Canvas1, text = '5', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label6 = tk.Label(Canvas1, text = '6', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label7 = tk.Label(Canvas1, text = '7', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label8 = tk.Label(Canvas1, text = '8', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Label9 = tk.Label(Canvas1, text = '9', fg ='#f0f0f0', width = 4, height = 2, borderwidth = 2, relief ='ridge')
Result = tk.Label(font = myFont2, anchor = 'center', width = 15)
Reset = tk.Button(text = '↩', command = ResetAll)

Label1.bind('<Button-1>',Obj().Dim)
Label2.bind('<Button-1>',Obj().Dim)
Label3.bind('<Button-1>',Obj().Dim)
Label4.bind('<Button-1>',Obj().Dim)
Label5.bind('<Button-1>',Obj().Dim)
Label6.bind('<Button-1>',Obj().Dim)
Label7.bind('<Button-1>',Obj().Dim)
Label8.bind('<Button-1>',Obj().Dim)
Label9.bind('<Button-1>',Obj().Dim)

Tittle.pack()
Canvas1.place(relx = 0.24, rely = 0.25 )
Label1.grid(column = 1, row = 1)
Label2.grid(column = 2, row = 1)
Label3.grid(column = 3, row = 1)
Label4.grid(column = 1, row = 2)
Label5.grid(column = 2, row = 2)
Label6.grid(column = 3, row = 2)
Label7.grid(column = 1, row = 3)
Label8.grid(column = 2, row = 3)
Label9.grid(column = 3, row = 3)
Result.place(relx = 0.14, rely = 0.82)


root.mainloop()


# -----------------------------------
# board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# def Win(sym):
#     i = 0
#     while(i<9):        
#         if(board[i]==sym and board[i+1]==sym and board[i+2]==sym):
#             return True
#         i = i+3
#     i =0
#     while(i<3):        
#         if(board[i]==sym and board[i+3]==sym and board[i+6]==sym):
#             return True
#         i = i+1
#     if((board[0]==sym and board[4]==sym and board[8]==sym) or (board[2]==sym and board[4]==sym and board[6]==sym)):
#         return True
#     return False

# def Layout():
#     print(" ",board[0],"|",board[1],"|",board[2])
#     print(" -----------")
#     print(" ",board[3],"|",board[4],"|",board[5])
#     print(" -----------")
#     print(" ",board[6],"|",board[7],"|",board[8])
#     print("\n\n")
# def Check(pos):
#     if(board[pos] == ' '):
#         board[pos] = 'X'
#         return 0
#     else:
#         return 1

# def Comp():
#     possible = []
#     for move in range(0,9):
#         if(board[move]==' '):
#             possible.append(move)

#     sym = ['O','X']
#     for x in sym:
#         for move in possible:
#             board[move] = x
#             if(Win(x)):
#                 board[move] = 'O'
#                 return
#             board[move] = ' '
#     board[random.choice(possible)] = 'O'
#     return

# def main():
#     check = 1
#     while(check):
#         position = int(input("Enter a valid position (1 -9):"))-1
#         check = Check(position)
#     Layout()
#     if(Win('X')):
#             print("\tYOU WIN !!!")
#             return
#     Comp()
#     Layout()
#     if(Win('O')):
#             print("\tBOT WINS !!!")
#             return
#     main()
#     print("G A M E  O V E R")