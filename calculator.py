# ----------------------------------------------------------------------
# Purpose:     Basic Calculator
# ----------------------------------------------------------------------
"""

"""
import tkinter
import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor

class Calculator:

    def __init__(self, parent):
        self.equation = ""
        parent.title("Calculator")

        self.canvas = tkinter.Canvas(parent, width=200, height=300)

        self.display = tkinter.Label(parent, text=self.equation, height=5)
        self.display.grid()

        #number buttons
        button_0 = tkinter.Button(self.canvas, text='0', command=lambda: self.update_equation("0"), width=5, height=3)
        button_1 = tkinter.Button(self.canvas, text='1', command=lambda: self.update_equation("1"), width=5, height=3)
        button_2 = tkinter.Button(self.canvas, text='2', command=lambda: self.update_equation("2"), width=5, height=3)
        button_3 = tkinter.Button(self.canvas, text='3', command=lambda: self.update_equation("3"), width=5, height=3)
        button_4 = tkinter.Button(self.canvas, text='4', command=lambda: self.update_equation("4"), width=5, height=3)
        button_5 = tkinter.Button(self.canvas, text='5', command=lambda: self.update_equation("5"), width=5, height=3)
        button_6 = tkinter.Button(self.canvas, text='6', command=lambda: self.update_equation("6"), width=5, height=3)
        button_7 = tkinter.Button(self.canvas, text='7', command=lambda: self.update_equation("7"), width=5, height=3)
        button_8 = tkinter.Button(self.canvas, text='8', command=lambda: self.update_equation("8"), width=5, height=3)
        button_9 = tkinter.Button(self.canvas, text='9', command=lambda: self.update_equation("9"), width=5, height=3)

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
        button_add = tkinter.Button(self.canvas, text='+', command=lambda: self.update_equation(" + "), width=5, height=3)
        button_sub = tkinter.Button(self.canvas, text='-', command=lambda: self.update_equation(" - "), width=5, height=3)
        button_mult = tkinter.Button(self.canvas, text='*', command=lambda: self.update_equation(" * "), width=5, height=3)
        button_div = tkinter.Button(self.canvas, text='/', command=lambda: self.update_equation(" / "), width=5, height=3)
        button_result = tkinter.Button(self.canvas, text='=', command=lambda: self.submit_equation(), width=5,height=3)
        button_clear = tkinter.Button(self.canvas, text='C', command=lambda: self.clear_equation(), width=5,height=3)

        button_add.grid(column=3, row=3)
        button_sub.grid(column=3, row=2)
        button_mult.grid(column=3, row=1)
        button_div.grid(column=3, row=0)
        button_result.grid(column=0, row=0)
        button_clear.grid(column=1, row=0)
        
        self.canvas.grid()

    def update_equation(self, value):
        self.equation += value
        self.display.config(text=self.equation)
        pass

    def clear_equation(self):
        self.equation = ""
        self.display.config(text=self.equation)

    def submit_equation(self):
        #pass to parser
        input_equation = InputStream(self.equation)

        lexer = ExprLexer(input_equation)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()

        res = MyExprVisitor().visitProg(tree)  # Evaluate the expression

        #update display with result
        self.display.config(text=res)
        pass

def main():
    root = tkinter.Tk() 
    Calculator(root)
    root.resizable(0,0)
    root.mainloop()    


if __name__ == '__main__':
    main()
