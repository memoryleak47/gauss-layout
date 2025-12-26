import pygame as pg

ELEMS = []

class Expr:
    def __add__(x, y):
        op = Op()
        op.lhs = x
        op.rhs = y
        op.op_str = "+"
        return op

    def __truediv__(x, y):
        op = Op()
        op.lhs = x
        op.rhs = y
        op.op_str = "/"
        return op

    def __sub__(x, y):
        op = Op()
        op.lhs = x
        op.rhs = y
        op.op_str = "-"
        return op

    def __mul__(x, y):
        op = Op()
        op.lhs = x
        op.rhs = y
        op.op_str = "*"
        return op

    def __eq__(x, y):
        eq = Equ()
        eq.lhs = x
        eq.rhs = y
        return eq

class Op(Expr):
    # lhs: Expr
    # rhs: Expr
    # op_str: str
    pass

class Var(Expr):
    pass

class Box:
    def __init__(self, text, color):
        ELEMS.append(self)

        self.left = Var()
        self.right = Var()
        self.top = Var()
        self.bot = Var()

        self.center_x = (self.left + self.right)/2
        self.center_y = (self.top + self.bot)/2
        self.width = self.right - self.left
        self.height = self.bot - self.top

        self.text = text
        self.color = color
        self.rect = pg.Rect(100, 200, 300, 400)

window = Box("", (100, 100, 100))

class Equ:
    # lhs: Expr
    # rhs: Expr
    pass

def constrain(eq: Equ):
    print(eq.lhs, eq.rhs)

# adds a .rect: pg.Rect
def compute_rects():
    pass

def run():
    compute_rects()

    pg.init()
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((255, 255, 255))
        
        for elem in ELEMS:
            pg.draw.rect(screen, elem.color, elem.rect)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
