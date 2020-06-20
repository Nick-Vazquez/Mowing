#####################################################
# Class to visualize mower movements across a plane #
# Uses Tkinter GUI package to draw mowable area,    #
# and highlights path covered.                      #
#####################################################

from tkinter import *


# Visualize mower movements around an area
# This area is passed to the class through the drawPoly method
class LawnVizualizer:
    # Set all class variables on instantiation, then create the canvas
    def __init__(self):
        # Define the class variables used
        self.canvas = None
        self.canvasSize = None
        self.root = None

        # Set up the window and canvas
        self.createCanvas()

        # Once the window is created, get accurate canvas size
        self.updateCanvasSize()

    # Define getter and setter methods for the root window
    def setCanvas(self, canvas):
        self.canvas = canvas

    def getCanvas(self):
        return self.canvas

    # Method to update the main root window
    def updateRoot(self):
        self.root.update()

    # Method to set the canvasSize class variable once created
    def updateCanvasSize(self):
        self.updateRoot()

        # Set the size of the canvas from the class canvas object
        self.canvasSize = [self.canvas.winfo_width(), self.canvas.winfo_height()]

    def createCanvas(self):
        # Create the window to place the application in
        root = Tk()

        # Get the screen size of the main window, set width
        # and height variables to fill a quarter of the screen
        width = (root.winfo_screenwidth() / 2)

        # Create the canvas inside of the root window and add it
        canvas = Canvas(root, width=width, height=width)
        canvas.pack()

        # Set the background of the canvas to black
        canvas.configure(background='black')

        self.root = root
        self.canvas = canvas

    def mainloop(self):
        self.root.mainloop()

    def drawPoly(self, points: list) -> NONE:
        # Check to see if the canvas has been defined
        if self.canvas:
            canvas = self.canvas
        else:
            raise AssertionError("Class Canvas has not been defined!")

        # Create a polygon of the points defined
        canvas.create_polygon(points, outline='green')

    # Take the input of unmapped width/height points on a scale of 0-100
    # and map these points to real coordinate points on the canvas
    # by using the real canvas width and height
    def mapPoints(self, unmappedPoints: list) -> list:
        # Get the latest canvas size
        self.updateCanvasSize()

        # Assert that the canvas size was of the right size
        if not len(self.canvasSize) == 2:
            raise AssertionError("List size does not match expected length!")

        # Create an empty list that will hold our final coordinates
        mappedPoints = []

        # Iterate over all lists within unmappedPoints list
        for point in unmappedPoints:
            # Assert that coordinates within the point are the right size
            if not len(point) == 2:
                raise AssertionError("List size does not match expected length!")

            mappedWidth = (point[0]) * (self.canvasSize[0] / 100)
            mappedHeight = (100 - point[1]) * (self.canvasSize[0] / 100)

            mappedPoints.append(mappedWidth)
            mappedPoints.append(mappedHeight)

        return mappedPoints


lawn = LawnVizualizer()

lawnPoints = [[10, 10], [20, 10], [20, 20], [90, 20], [90, 90], [10, 90]]

mappedPoints = lawn.mapPoints(lawnPoints)

lawn.drawPoly(mappedPoints)

lawn.mainloop()
