import gauss as gs

b1 = gs.Box((255, 0, 0))
b2 = gs.Box((0, 255, 0))
b3 = gs.Box((0, 0, 255))

# All boxes have the same height, namely a third of the window height
h = gs.Var()
gs.equate(b1.height, h)
gs.equate(b2.height, h)
gs.equate(b3.height, h)

gs.equate(h, gs.window.height/3)

# They are y-centered
gs.equate(b1.center_y, gs.window.center_y)
gs.equate(b2.center_y, gs.window.center_y)
gs.equate(b3.center_y, gs.window.center_y)

# They have spaces of 10 in between and fill the entire x-space
gs.equate(b1.left, gs.window.left + 10)
gs.equate(b1.right + 10, b2.left)
gs.equate(b2.right + 10, b3.left)
gs.equate(b3.right + 10, gs.window.right)

# They have the same width
gs.equate(b1.width, b2.width)
gs.equate(b1.width, b3.width)

# Show it!
gs.run()
