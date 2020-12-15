#!/usr/bin/python
# Kyle Arnold
# Programming for IT Final - Tic Tac Toe GUI
# 11/27/20




import random                                  # Import modules needed for program
from tkinter import messagebox
from tkinter import *


window = Tk()                                  # Create a window
window.title("Tic Tac Toe")                    # Name the window "Tic Tac Toe"

Click = True                                   # The Click variable is used to determine who's turn it is
Plays = 0                                      # The Plays variable is used to detect a tie

# The lambda function used here is used to point to a function with a parameter. Here, it is Button 1.
Button1 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button1))   
Button1.grid(row = 3, column = 0)

Button2 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button2))
Button2.grid(row=3, column=1)

Button3 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button3))
Button3.grid(row=3, column=2)

Button4 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button4))
Button4.grid(row=4, column=0)

Button5 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button5))
Button5.grid(row=4, column=1)

Button6 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button6))
Button6.grid(row=4, column=2)

Button7 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button7))
Button7.grid(row=5, column=0)

Button8 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button8))
Button8.grid(row=5, column=1)

Button9 = Button(window, text = ' ', font = 'Arial 20', bg = 'white', fg = 'black', height = 2, width = 4, command = lambda: PlayerMove(Button9))
Button9.grid(row=5, column=2)

Buttons = [Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Button9]    # Gather the buttons into a list called Buttons

def PlayerMove(Buttons):                              # The game will always start on user's turn

    global Plays, Click                               # Call in the variables for the user

    print('Player Move')
    if Buttons['text'] == " " and Click == True:
        print('Number of Plays ' + str(Plays))        # Diagnostic for counting the amount of plays
        Buttons['text'] = "X"                         # Changed the buttons text to "X"
        Click = False                                 # Set Click to false, making it the computer's turn
        Plays += 1                                    # Add 1 to Plays variable
        WinCheck(Click, Buttons)                      # Go to WinCheck, this will happen after every user move


def CompRow(Buttons):

    print('Row')                               # Diagnostic showing computer is checking rows
    global Click
    Click = True                               # Set click to true, once the computer reaches a verdict, it is user's turn
    Row1 = [Button1, Button2, Button3]         # Create list for the rows of buttons
    Row2 = [Button4, Button5, Button6]
    Row3 = [Button7, Button8, Button9]
    Row1countX = 0                             # Variables needed to determine if to win or to block
    Row1countO = 0
    Row2countX = 0
    Row2countO = 0
    Row3countX = 0
    Row3countO = 0

    for Button in Row1:                        # Loop through Row1
        if Button['text'] == 'X':              # If the button contains an X, add 1 to the Row1countX
            Row1countX += 1
        elif Button['text'] == 'O':            # If the button contains an O, add 1 to the Row1countO
            Row1countO += 1

    if Row1countX == 0 and Row1countO == 2:    # Winning move, if computer detects one more spot needs an O, place it.
        for Button in Row1:
            if Button['text'] == " ":          # Find empty button
                Button['text'] = "O"           # Place an O
                CompWins()                     # Go to CompWins function

    elif Row1countX == 2 and Row1countO == 0:  # Blocking move, if computer detects one more spot needs an X, block it.
        for Button in Row1:
            if Button['text'] == " ":          # Whatever button was blank, place O there
                Button['text'] = "O"
                print('block')                 # Diagnostic showing computer has blocked
                break

        PlayerMove(Buttons)                    # After loop, if block condition was met, it is the player's turn
        return
    else:
        pass                                   # If there is only 1 spot taken, move on to Row2

    for Button in Row2:                        # Same as above for loop for Row1 but for Row2

        if Button['text'] == 'X':
            Row2countX += 1
        elif Button['text'] == 'O':
            Row2countO += 1

    if Row2countX == 0 and Row2countO == 2:    # Winning move
        for Button in Row2:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Row2countX == 2 and Row2countO == 0:  # Blocking move
        for Button in Row2:
            if Button['text'] == " ":
                Button['text'] = "O"
                break

        PlayerMove(Buttons)
        return
    else:
        pass                                   # If there is only 1 spot taken, move to Row3

    for Button in Row3:                        # Same as above for loop for Row2 but for Row3

        if Button['text'] == 'X':
            Row3countX += 1
        elif Button['text'] == 'O':
            Row3countO += 1

    if Row3countX == 0 and Row3countO == 2:    # Winning move
        for Button in Row3:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Row3countX == 2 and Row3countO == 0:  # Blocking move
        for Button in Row3:
            if Button['text'] == " ":
                Button['text'] = "O"
                break

        PlayerMove(Buttons)
        return
    else:                                      # If there are not any good moves, check columns
        CompColumn(Buttons)


def CompColumn(Buttons):                                   # This function is same as CompRow, except the list for the buttons is now in a column.

    print('Column')                                        # Diagnostic showing computer is checking columns
    Column1 = [Button1, Button4, Button7]                  # Create lists for the columns of buttons
    Column2 = [Button2, Button5, Button8]
    Column3 = [Button3, Button6, Button9]
    Column1countX = 0                                      # Variables needed to determine if to win or to block
    Column1countO = 0
    Column2countX = 0
    Column2countO = 0
    Column3countX = 0
    Column3countO = 0

    for Button in Column1:                                 # Loop through column 1

        if Button['text'] == 'X':                          # If button is X, add 1 to Column1countX
            Column1countX += 1
        elif Button['text'] == 'O':                        # If button is O, add 1 to Column1countO
            Column1countO += 1

    if Column1countX == 0 and Column1countO == 2:          # Winning move
        for Button in Column1:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Column1countX == 2 and Column1countO == 0:        # Blocking move
        for Button in Column1:
            if Button['text'] == " ":
                Button['text'] = "O"

        PlayerMove(Buttons)
        return
    else:
        pass                                               # If only 1 spot is taken, move to Column2

    for Button in Column2:

        if Button['text'] == 'X':
            Column2countX += 1
        elif Button['text'] == 'O':
            Column2countO += 1

    if Column2countX == 0 and Column2countO == 2:          # Winning move
        for Button in Column2:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Column2countX == 2 and Column1countO == 0:        # Blocking move
        for Button in Column2:
            print("Column2")
            if Button['text'] == " ":
                Button['text'] = "O"
                PlayerMove(Buttons)
        return
    else:
        pass                                               # If only 1 spot is taken, move to Column3

    for Button in Column3:                                 # Loop through Column3
        print("Column3")
        if Button['text'] == 'X':
            Column3countX += 1
        elif Button['text'] == 'O':
            Column3countO += 1

    if Column3countX == 0 and Column3countO == 2:          # Wining move
        for Button in Column3:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Column3countX == 2 and Column1countO == 0:        # Blocking move
        for Button in Column3:
            if Button['text'] == " ":
                Button['text'] = "O"

        PlayerMove(Buttons)
        return
    else:
        CompDiagonal(Buttons)

def CompDiagonal(Buttons):

    print('Diagonal')                                           # Diagnostic showing computer is checking diagonals
    Diagonal1 = [Button1, Button5, Button9]
    Diagonal2 = [Button3, Button5, Button7]
    Diagonal1countX = 0
    Diagonal1countO = 0
    Diagonal2countX = 0
    Diagonal2countO = 0

    for Button in Diagonal1:
        if Button['text'] == 'X':
            Diagonal1countX += 1
        elif Button['text'] == 'O':
            Diagonal1countO += 1

    if Diagonal1countX == 0 and Diagonal1countO == 2:           # Winning move
        for Button in Diagonal1:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Diagonal1countX == 2 and Diagonal1countO == 0:         # Blocking move
        for Button in Diagonal1:
            if Button['text'] == " ":
                Button['text'] = "O"

        PlayerMove(Buttons)
        return
    else:
        pass                                                    # If no good moves, move to Diagonal2

    for Button in Diagonal2:

        if Button['text'] == 'X':
            Diagonal2countX += 1
        elif Button['text'] == 'O':
            Diagonal2countO += 1

    if Diagonal2countX == 0 and Diagonal2countO == 2:           # Winning move
        for Button in Diagonal2:
            if Button['text'] == " ":
                Button['text'] = "O"
                CompWins()

    elif Diagonal2countX == 2 and Diagonal2countO == 0:         # Blocking move
        for Button in Diagonal2:
            if Button['text'] == " ":
                Button['text'] = "O"

        PlayerMove(Buttons)
        return
    else:
        RandomMove(Buttons)


def RandomMove(Buttons):                                        # Straight forward random loop

    Choice = random.randint(1, 9)                               # Choose a number 1-9, name it Choice
    if Choice == 1 and Button1["text"] == " ":                  # If the number is 1 and the box is blank, place an O
        Button1["text"] = "O"                                   # Same for the other 8 choices below
        PlayerMove(Buttons)
    elif Choice == 2 and Button2["text"] == " ":
        Button2["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 3 and Button3["text"] == " ":
        Button3["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 4 and Button4["text"] == " ":
        Button4["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 5 and Button5["text"] == " ":
        Button5["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 6 and Button6["text"] == " ":
        Button6["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 7 and Button7["text"] == " ":
        Button7["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 8 and Button8["text"] == " ":
        Button8["text"] = "O"
        PlayerMove(Buttons)
    elif Choice == 9 and Button9["text"] == " ":
        Button9["text"] = "O"
        PlayerMove(Buttons)
    else:
        RandomMove(Buttons)


def WinCheck(Click, Buttons):
    if (Button1['text'] == 'X' and Button2['text'] == 'X' and Button3['text'] == 'X' or            # Row1
        Button4['text'] == 'X' and Button5['text'] == 'X' and Button6['text'] == 'X' or            # Row2
        Button7['text'] == 'X' and Button8['text'] == 'X' and Button9['text'] == 'X' or            # Row3
        Button1['text'] == 'X' and Button4['text'] == 'X' and Button7['text'] == 'X' or            # Column1
        Button2['text'] == 'X' and Button5['text'] == 'X' and Button8['text'] == 'X' or            # Column2
        Button3['text'] == 'X' and Button6['text'] == 'X' and Button9['text'] == 'X' or            # Column3
        Button1['text'] == 'X' and Button5['text'] == 'X' and Button9['text'] == 'X' or            # Diagonal1
        Button3['text'] == 'X' and Button5['text'] == 'X' and Button7['text'] == 'X'):             # Diagonal2
        PlayerWins()

    elif Plays == 5:                 # The user can only make 5 plays. Once reached, game is considered a tie.

        messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        exit()

    elif Click == False:
        CompRow(Buttons)
    else:
        PlayerMove(Buttons)


def PlayerWins():                                               # Player has won
    messagebox.showinfo('Tic Tac Toe', 'You have won!')         # Display message that player has won
    exit()


def CompWins():                                                 # Computer has won
    messagebox.showinfo('Tic Tac Toe', 'You have lost!')        # Display message that computer has won
    exit()


window.mainloop()
