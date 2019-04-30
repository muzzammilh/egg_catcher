from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

# Various game settings
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 400
CANVAS_BACKGROUND = 'deep sky blue'
GRASS_COLOR = 'sea green'
SUN_COLOR = 'orange'
COLOR_CYCLE = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])

# Create a window.
root = Tk()

# Create canvas
c = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_BACKGROUND)

# Create some grass on the canvas bottom
c.create_rectangle(-5, CANVAS_HEIGHT - 100, CANVAS_WIDTH + 5, CANVAS_HEIGHT + 5, fill=GRASS_COLOR, width=0)

# Create a sun in top left corner
c.create_oval(-80, -80, 120, 120, fill=SUN_COLOR, width=0)

# Combine everything and draw
c.pack()
c.mainloop()
