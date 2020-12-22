Kyle Arnold - 00300492
Programming for IT - Final - Tic Tac Toe GUI
12/21/20

This program is the classic Tic Tac Toe game but instead of using a command line to interact, you can click buttons instead. I wanted
to learn how to start making basic GUI programs as I want to develop some apps for gaming that I can use to improve the experience.


Completion Statement:

I was able to write the program and get it to work with only a small amount of bugs:

1. Sometimes the computer will not make a move, this seems to happen at random and I can't replicate it enough to isolate the problem.
2. If the computer populates the middle and right column, sometimes a win detection does not work. 
3. Sometimes the computer will choose a random move instead of blocking like it is supposed to.

Statement of Assistance:

My sister's fiancee Josh helped me with debugging and also showed me how to use the debugger in PyCharm.

Sites I used for information:

https://www.w3schools.com/python/
https://www.geeksforgeeks.org/python-programming-language/

------------------------------------------------------------------

Instructions:

The program is very simple to operate. Once the program is launched, it will always be the players turn.
There are 9 buttons to choose from in a 3x3 grid, just like a Tic Tac Toe board.
The objective is to win by lining 3 x's in a row, column, or diagonal.

Keep in mind that the computer will always try to block you, so it is best to try and set up a "two-way"
winning move since the computer can only block one of the ways to win.


Dependencies:

Modules - tkinter, random, os, and datetime

Tkinter is used to generate the window and buttons for the game.
Random is used to select a random move for the computer if needed.
Os is used to generate the folder "Game Recordings" and place a file in the folder.
Datetime is used to get the time and name the recorded game file after the current time.


Future Work:

I am actually really satisfied that I was able to get this far with the program. The idea of trying to make a GUI
was daunting, but after a little research I saw that it really was not so bad. I am however a bit annoyed that 
I could not figure out the bugs I listed in the completetion statement as I was running out of time. Otherwise,
I would have figured out why these bugs were occuring and fixed them.  

