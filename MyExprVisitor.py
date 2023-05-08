from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.stack = []  # Stack to evaluate the expression
        self.divided_by_zero = False

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visit(ctx.expr())  # Just visit the self expression

    # Visit a parse tree produced by ExprParser#infixExpr.
    def visitInfixExpr(self, ctx:ExprParser.InfixExprContext):
        # if self.divided_by_zero:
        #     return "Can't divide by zero!"
        self.visit(ctx.left)  # Evaluate the left  expression and push to stack
        self.visit(ctx.right) # Evaluate the right expression and push to stack

        check = self.stack[-1]
        if check == "Can't divide by zero!":
            return "Can't divide by zero!"
        b = self.stack.pop()  # Why is ‘b’ the first popped item?
        a = self.stack.pop()
        c = None

        if ctx.OP_EXP():
            c = a ** b
        elif ctx.OP_MUL():
            c = a * b
        elif ctx.OP_DIV():
            try:
                c = a / b
            except ZeroDivisionError:
                c = "Can't divide by zero!"
                self.divided_by_zero = True
        elif ctx.OP_ADD():
            c = a + b
        elif ctx.OP_SUB():
            c = a - b


        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        if self.divided_by_zero:
            return
        c = int(str(ctx.INT()))  # Found a number, just insert to stack
        self.stack.append(c)
        return c

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx:ExprParser.ParensExprContext):
        return self.visit(ctx.expr())  # Since enclosed by parents, just visit expr

    def visitNegNumberExpr(self, ctx: ExprParser.NegNumberExprContext):
        c = -int(str(ctx.INT()))  # Found a negative number, insert its negative value to stack
        self.stack.append(c)
        return c