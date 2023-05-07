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
import re

class Calculator:

    def __init__(self, parent):
        self.equation = "0"
        self.just_calculated = False
        self.result = ""
        self.cleared = True
        parent.title("Calculator")

        self.canvas = tkinter.Canvas(parent, width=200, height=300)

        self.display = tkinter.Label(parent, text=self.equation, height=5)
        self.display.grid()

        #number buttons
        button_0 = tkinter.Button(self.canvas, text='0', command=lambda: self.update_number("0"), width=5, height=3)
        button_1 = tkinter.Button(self.canvas, text='1', command=lambda: self.update_number("1"), width=5, height=3)
        button_2 = tkinter.Button(self.canvas, text='2', command=lambda: self.update_number("2"), width=5, height=3)
        button_3 = tkinter.Button(self.canvas, text='3', command=lambda: self.update_number("3"), width=5, height=3)
        button_4 = tkinter.Button(self.canvas, text='4', command=lambda: self.update_number("4"), width=5, height=3)
        button_5 = tkinter.Button(self.canvas, text='5', command=lambda: self.update_number("5"), width=5, height=3)
        button_6 = tkinter.Button(self.canvas, text='6', command=lambda: self.update_number("6"), width=5, height=3)
        button_7 = tkinter.Button(self.canvas, text='7', command=lambda: self.update_number("7"), width=5, height=3)
        button_8 = tkinter.Button(self.canvas, text='8', command=lambda: self.update_number("8"), width=5, height=3)
        button_9 = tkinter.Button(self.canvas, text='9', command=lambda: self.update_number("9"), width=5, height=3)

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
        button_add = tkinter.Button(self.canvas, text='+', command=lambda: self.update_operator(" + "), width=5, height=3)
        button_sub = tkinter.Button(self.canvas, text='-', command=lambda: self.update_operator(" - "), width=5, height=3)
        button_mult = tkinter.Button(self.canvas, text='*', command=lambda: self.update_operator(" * "), width=5, height=3)
        button_div = tkinter.Button(self.canvas, text='/', command=lambda: self.update_operator(" / "), width=5, height=3)
        button_result = tkinter.Button(self.canvas, text='=', command=lambda: self.submit_equation(), width=5,height=3)
        button_clear = tkinter.Button(self.canvas, text='C', command=lambda: self.clear_equation(), width=5,height=3)

        button_add.grid(column=3, row=3)
        button_sub.grid(column=3, row=2)
        button_mult.grid(column=3, row=1)
        button_div.grid(column=3, row=0)
        button_result.grid(column=0, row=0)
        button_clear.grid(column=1, row=0)
        
        self.canvas.grid()

    def update_number(self, value):
        if self.just_calculated:
            self.equation = ""
        self.just_calculated = False
        self.cleared = False
        self.equation += value
        self.display.config(text=self.equation)
        pass

    def update_operator(self, value):
        # if self.cleared:
        #     self.equation = "0"
        # elif self.just_calculated:
        #     self.equation = self.result
        self.just_calculated = False
        self.cleared = False
        self.equation += value
        self.display.config(text=self.equation)
        pass

    def clear_equation(self):
        self.equation = "0"
        self.display.config(text=self.equation)
        self.just_calculated = True
        self.cleared = True

    def submit_equation(self):
        #strip any extra operators
        stripped = re.sub(r"\D+$", "", self.equation)
        
        #pass to parser
        input_equation = InputStream(stripped)

        lexer = ExprLexer(input_equation)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()

        self.result = str(MyExprVisitor().visitProg(tree))  # Evaluate the expression

        #update display with result
        self.display.config(text=self.result)
        self.just_calculated = True
        self.cleared = False
        self.equation = "0"
        pass

def main():
    root = tkinter.Tk() 
    Calculator(root)
    root.resizable(0,0)
    root.mainloop()    


if __name__ == '__main__':
    main()
