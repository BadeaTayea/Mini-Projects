import turtle
import math

def drawTriangle(t, points, color):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def Mid(p1,p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierpinski(t, N, points):
    colormap = ['white']
    for i in range(N):
        colormap.append("black")

    drawTriangle(t, points, colormap[N])
    if N > 0:
        sierpinski(t, N-1, [points[0], Mid(points[0], points[1]), Mid(points[0], points[2])])
        sierpinski(t, N-1, [points[1], Mid(points[0], points[1]), Mid(points[1], points[2])])
        sierpinski(t, N-1, [points[2], Mid(points[2], points[1]), Mid(points[0], points[2])])

def main():
   N = int(input("Number of iterations: "))
   t = turtle.Turtle()
   t.speed("slow")
   screen = turtle.Screen()
   screen.setworldcoordinates(0, 0, 1, math.sqrt(3) / 2)
   Points = [[0, 0], [1, 0], [0.5, math.sqrt(3) / 2]]
   sierpinski(t, N, Points)
   screen.exitonclick()

main()


# Helper Functions
# Function for turning given x and y coordinates to a list of points:
# def points(x, y):
#   Points = []
#   p1 = [x[0], y[0]]
#   p2 = [x[1], y[1]]
#   p3 = [x[2], y[2]]
#
#   return [p1, p2, p3]

# Function for turning list of points back to seperate coordinate:
# def coordinates(points):
#   xCoors = []
#   yCoors = []
#   for i in points:
#     xCoors.append(i[0])
#     yCoors.append(i[1])
#   return xCoors, yCoors
