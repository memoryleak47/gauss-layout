import pygame as pg
import sympy

ELEMS = []
VARS = []
CONSTRAINTS = []

class Expr:
    # coeffs: Var -> number
    # offset: number
    def __init__(self):
        self.coeffs = dict()
        self.offset = 0

    def to_expr(a):
        if isinstance(a, Expr):
            return a
        if isinstance(a, (float, int)):
            e = Expr()
            e.offset = a
            return e
        raise "ohno"

    def __add__(x, y):
        y = Expr.to_expr(y)
        assert(isinstance(y, Expr))

        out = Expr()
        for v in VARS:
            xc = x.coeffs[v] if v in x.coeffs else 0
            yc = y.coeffs[v] if v in y.coeffs else 0
            out.coeffs[v] = xc + yc
        out.offset = x.offset + y.offset
        return out

    def __mul__(x, y):
        assert(isinstance(y, (int, float)))
        out = Expr()
        for (a, c) in x.coeffs.items():
            out.coeffs[a] = c*y
        out.offset = x.offset * y
        return out

    def __truediv__(x, y):
        return x * (1/y)

    def __sub__(x, y):
        return x + (y * (-1))

class Var(Expr):
    def __init__(self):
        self.coeffs = dict()
        self.coeffs[self] = 1
        self.offset = 0
        VARS.append(self)

class Box:
    def __init__(self, color):
        ELEMS.append(self)

        self.left = Var()
        self.right = Var()
        self.top = Var()
        self.bot = Var()

        self.center_x = (self.left + self.right)/2
        self.center_y = (self.top + self.bot)/2
        self.width = self.right - self.left
        self.height = self.bot - self.top

        self.color = color

def equate(lhs, rhs):
    sub = lhs - rhs
    CONSTRAINTS.append(sub)

window = Box((0, 0, 0))
equate(window.left, 0)
equate(window.top, 0)
equate(window.right, 800)
equate(window.bot, 600)

def ev(coeffs, d):
    s = 0
    for (v, c) in coeffs.items():
        s += d[v] * c
    return int(s)

# adds a .rect: pg.Rect
def compute_rects():
    symvars = sympy.symbols('v:' + str(len(VARS)))

    def to_sym(v):
        i = VARS.index(v)
        return symvars[i]

    eqs = []
    for t in CONSTRAINTS:
        s = t.offset
        s += sum([to_sym(v)*c for v, c in t.coeffs.items()])
        eqs.append(s)

    sol = sympy.solve(eqs)
    d = dict()
    # This will fail if the system is under-, or over-specified.
    for i, v in enumerate(VARS):
        d[v] = sol[symvars[i]]
    for e in ELEMS:
        l = ev(e.left.coeffs, d)
        t = ev(e.top.coeffs, d)
        w = ev(e.width.coeffs, d)
        h = ev(e.height.coeffs, d)
        e.rect = pg.Rect(l, t, w, h)

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
