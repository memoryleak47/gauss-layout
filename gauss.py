import pygame as pg

ELEMS = []
VARS = []
CONSTRAINTS = []

class Expr:
    def __init__(self):
        self.coeffs = dict()

    # coeffs: Var -> number
    def __add__(x, y):
        assert(isinstance(y, Expr))

        out = Expr()
        for v in VARS:
            xc = x.coeffs[v] if v in x.coeffs else 0
            yc = y.coeffs[v] if v in y.coeffs else 0
            out.coeffs[v] = xc + yc
        return out

    def __mul__(x, y):
        assert(isinstance(y, (int, float)))
        out = Expr()
        for (a, c) in x.coeffs.items():
            out.coeffs[a] = c*y
        return out

    def __truediv__(x, y):
        return x * (1/y)

    def __sub__(x, y):
        return x + (y * (-1))

class Var(Expr):
    def __init__(self):
        self.coeffs = dict()
        self.coeffs[self] = 1
        VARS.append(self)

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

window = Box("", (100, 100, 100))

def equate(lhs, rhs):
    print(lhs, rhs)
    CONSTRAINTS.append((lhs, rhs))

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
