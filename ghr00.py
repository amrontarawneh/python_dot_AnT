from graphics import *

def main():
    # 1. Create a graphical window
    win = GraphWin("Py_Control Graphics", 500, 500)

    # 2. Draw a Circle
    center = Point(250, 250)

    circ = Circle(center, 50)
    circ.setFill("red")
    circ.setOutline("black")
    circ.draw(win)

    # 3. Add Text
    label = Text(Point(250, 320), "Click anywhere to close")
    label.draw(win)

    # 4. Interaction
    win.getMouse()

    # Shut down the window
    win.close()


main()