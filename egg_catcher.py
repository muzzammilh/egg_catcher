from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

# Various game settings
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
CANVAS_BACKGROUND = 'deep sky blue'
GRASS_COLOR = 'sea green'
SUN_COLOR = 'orange'

COLOR_CYCLE = cycle(['light blue', 'light green', 'light pink', 'light yellow', 'light cyan'])
EGG_WIDTH = 45
EGG_HEIGHT = 55
EGG_SCORE = 10
EGG_SPEED = 500
EGG_INTERVAL = 4000
DIFFICULTY_FACTOR = 0.95

CATCHER_COLOR = 'blue'
CATCHER_WIDTH = 100
CATCHER_HEIGHT = 100


# Create a window.
root = Tk()

# Create canvas
c = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_BACKGROUND)

# Create some grass on the canvas bottom
c.create_rectangle(-5, CANVAS_HEIGHT - 100, CANVAS_WIDTH + 5, CANVAS_HEIGHT + 5, fill=GRASS_COLOR, width=0)

# Create a sun in top left corner
c.create_oval(-80, -80, 120, 120, fill=SUN_COLOR, width=0)

# Create catcher
catcher_start_x = CANVAS_WIDTH / 2 - CATCHER_WIDTH / 2
catcher_start_y = CANVAS_HEIGHT - CATCHER_HEIGHT - 20
catcher_start_x2 = catcher_start_x + CATCHER_WIDTH
catcher_start_y2 = catcher_start_y + CATCHER_HEIGHT

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, start=200, extend=140,
                       style='arc', outline=CATCHER_COLOR, width=3)

# Combine everything and draw
c.pack()
c.mainloop()
