import gauss as gs

b1 = gs.Box("nice", (255, 0, 0))
b2 = gs.Box("wow", (0, 0, 255))

gs.equate(b1.right, b2.left)

gs.run()
