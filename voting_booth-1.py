from tkinter import*

top = Tk()
top['bg'] = 'white'

# First Frame    
frame1 = Frame(top, bg = 'Black')
frame1.pack(side = 'top')
Label(frame1, text = 'Vote for your favorite movie!', \
      fg = 'black', bg = 'light blue', font = 'size 18').pack(side = TOP)

# Second Frame
frame2 = Frame(top, bg = 'black')
frame2.pack(side = 'top')

Label(frame2, text = 'MOVIE', fg = 'cyan', bg = 'Black').grid(row = 0, column = 0, ipadx = 30)
Label(frame2, text = 'VOTES', fg = 'cyan', bg = 'Black').grid(row = 0, column = 1, ipadx = 30)

# Global variables
max_vote = 0
name = "Tied"

x_1 = 0
x_2 = 0
x_3 = 0
x_4 = 0

def clicker(label_n, button_n):
    """With every click on button_n, the value of the corresponding label_n is increased by one,
       the max_vote is updated whenever a "vote button" is clicked, so is the name_label.
    """ 
    x = label_n.cget("text")
    x = x + 1
    label_n.config(text = x)
    global max_vote
    if max_vote < x:
        max_vote = x
        name_label["text"] = button_n.cget("text")
    elif max_vote == x:
        name_label["text"] =  "Tied"


label_1 = Label(frame2, text = x_1, font = 'size 10', width = 10, bg = 'blue', fg = 'white')
label_1.grid(row = 1, column = 1)
button_1 = Button(frame2, text = 'Kill Bill', width = 20, fg = 'red', bg = 'green', command = lambda: clicker(label_1, button_1)) # lambda is used here to pass parameters
button_1.grid(row = 1, column = 0)

label_2 = Label(frame2, text = x_2, font = 'size 10', width = 10, bg = 'blue', fg = 'white')
label_2.grid(row = 2, column = 1)
button_2 = Button(frame2, text = 'The Hateful Eight', width = 20, fg = 'red', bg = 'green', command = lambda: clicker(label_2, button_2))
button_2.grid(row = 2, column = 0)

label_3 = Label(frame2, text = x_3, font = 'size 10', width = 10, bg = 'blue', fg = 'white')
label_3.grid(row = 3, column = 1)
button_3 = Button(frame2, text = 'Pulp Fiction', width = 20, fg = 'red', bg = 'green', command = lambda: clicker(label_3, button_3))
button_3.grid(row = 3, column = 0)

label_4 = Label(frame2, text = x_2, font = 'size 10', width = 10, bg = 'blue', fg = 'white')
label_4.grid(row = 4, column = 1)
button_4 = Button(frame2, text = 'Reservoir Dogs', width = 20, fg = 'red', bg = 'green', command = lambda: clicker(label_4, button_4))
button_4.grid(row = 4, column = 0)

# Need to evaluate max_vote after each click!
last_label = Label(frame2, text = "winner so far: ", font = 'size 15', width = 15, bg = 'cyan', fg = 'red').grid(row = 5, column = 0, ipadx = 20, pady = 10)
name_label = Label(frame2, text = name, font = 'size 15', width = 20, bg = 'cyan', fg = 'red')
name_label.grid(row = 5, column = 1, ipadx = 15, pady = 10)
 
top.mainloop()
