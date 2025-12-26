import gauss as gs

b1 = gs.Box((255, 0, 0))
b2 = gs.Box((0, 255, 0))
b3 = gs.Box((0, 0, 255))

# All boxes have the same height, namely a third of the window height
h = gs.Var()
gs.add(b1.height == h)
gs.add(b2.height == h)
gs.add(b3.height == h)

gs.add(h == gs.window.height/3)

# They are y-centered
gs.add(b1.center_y == gs.window.center_y)
gs.add(b2.center_y == gs.window.center_y)
gs.add(b3.center_y == gs.window.center_y)

# In x-direction, the boxes are positioned in sequence.
in_gap = gs.Var() # Gap between consecutive boxes
out_gap = gs.Var() # Gap between window border and box

gs.add(b1.left == gs.window.left + out_gap)
gs.add(b1.right + in_gap == b2.left)
gs.add(b2.right + in_gap == b3.left)
gs.add(b3.right + out_gap == gs.window.right)

gs.add(in_gap == out_gap / 2) # the distance to the border should be double of the distance between boxes
gs.add(h == in_gap*4) # the gap between elements shall be a fourth of the height of the boxes

# Each consecutive box doubles in size
gs.add(b1.width*2 == b2.width)
gs.add(b2.width*2 == b3.width)

# Show it!
gs.run()
