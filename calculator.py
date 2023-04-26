# ----------------------------------------------------------------------
# Purpose:     Basic Calculator
# ----------------------------------------------------------------------
"""

"""
import tkinter

class Calculator:

    def __init__(self, parent):
        parent.title("Calculator")

        self.canvas = tkinter.Canvas(parent, width=200, height=300)

        display = tkinter.Label(parent, text="calculation here", height=5)
        display.grid()

        #number buttons
        button_0 = tkinter.Button(self.canvas,text='0', width=4,height=4)
        button_1 = tkinter.Button(self.canvas,text='1', width=4,height=4)
        button_2 = tkinter.Button(self.canvas,text='2', width=4,height=4)
        button_3 = tkinter.Button(self.canvas,text='3', width=4,height=4)
        button_4 = tkinter.Button(self.canvas, text='4', width=4, height=4)
        button_5 = tkinter.Button(self.canvas, text='5', width=4, height=4)
        button_6 = tkinter.Button(self.canvas, text='6', width=4, height=4)
        button_7 = tkinter.Button(self.canvas, text='7', width=4, height=4)
        button_8 = tkinter.Button(self.canvas, text='8', width=4, height=4)
        button_9 = tkinter.Button(self.canvas, text='9', width=4, height=4)

        button_0.grid(column=2, row=0)
        button_1.grid(column=0, row=3)
        button_2.grid(column=1, row=3)
        button_3.grid(column=2, row=3)
        button_4.grid(column=0, row=2)
        button_5.grid(column=1, row=2)
        button_6.grid(column=2, row=2)
        button_7.grid(column=0, row=1)
        button_8.grid(column=1, row=1)
        button_9.grid(column=2, row=1)

        # operation buttons
        button_add = tkinter.Button(self.canvas, text='+', width=4, height=4)
        button_sub = tkinter.Button(self.canvas, text='-', width=4, height=4)
        button_mult = tkinter.Button(self.canvas, text='*', width=4, height=4)
        button_div = tkinter.Button(self.canvas, text='/', width=4, height=4)
        button_result = tkinter.Button(self.canvas, text='=',width=4,height=4)
        button_clear = tkinter.Button(self.canvas, text='C', width=4,height=4)

        button_add.grid(column=3, row=3)
        button_sub.grid(column=3, row=2)
        button_mult.grid(column=3, row=1)
        button_div.grid(column=3, row=0)
        button_result.grid(column=0,row=0)
        button_clear.grid(column=1, row=0)
        
        self.canvas.grid()



def main():
    root = tkinter.Tk() 
    Calculator(root)
    root.resizable(0,0)
    root.mainloop()    


if __name__ == '__main__':
    main()
