import gauss as gs

b1 = gs.Box("nice", (255, 0, 0))

gs.equate(b1.left - gs.window.left, gs.window.right - b1.right)
gs.equate(b1.top, 0)
gs.equate(b1.bot, gs.window.height / 2)
gs.equate(b1.width, b1.height)

gs.run()
