
# Import the turtle module and math module
import turtle
import math

# Constants (you can change these)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Digital String Art by Anushka"

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)
screen.bgcolor("indigo")

# Create the turtle object
screw = turtle.Turtle()

#starting with turtle
screw.hideturtle()
screw.up()

#input for number of screws
screw_num = int(screen.numinput(screw, "Enter the total number of Screws: "))

#location of the nail

#nail 1
x_coord_1 = screen.numinput(screw, "Enter the x coordinate of the Screw: ")
y_coord_1 = screen.numinput(screw, "Enter the y coordinate of the Screw: ")
screw.goto(x_coord_1,y_coord_1)
screw.down()

#for making the string
x_coord_2=x_coord_1
y_coord_2=y_coord_1

#for calculating with distance formula
x1=x_coord_1
y1=y_coord_1

#input and loop
total_length = 0
for i in range(screw_num - 1):
    
    #makes nail
    screw.pencolor("blue")
    screw.down()
    screw.dot(5)
    screw.up() 
    
    #input
    screw_x_coord = screen.numinput(screw, "Enter the x coordinate of the Screw: ")
    screw_y_coord = screen.numinput(screw, "Enter the y coordinate of the Screw: ")
   
    #final location of nail for last string
    final_x = screw_x_coord
    final_y = screw_y_coord
    
    #makes next nail and then the string
    screw.goto(screw_x_coord,screw_y_coord)
    screw.down()
    screw.dot(5)
    screw.up()
    screw.goto(x_coord_2,y_coord_2)
    screw.down()
    screw.width(3)
    screw.pencolor("red")
    screw.goto(screw_x_coord,screw_y_coord)
    screw.up()
    
    #making the nails above the string
    screw.pencolor("blue")
    screw.goto(x_coord_2,y_coord_2)
    screw.down()
    screw.dot(5)
    screw.up()
    
    #storing the final location to make the string in next round
    x_coord_2=screw_x_coord
    y_coord_2=screw_y_coord
    
    #calculating the distance between 2 points(length of string)
    x2 = screw_x_coord 
    y2 = screw_y_coord 
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    #keeping track of total length
    total_length = total_length + distance
    
    #making second point from previous code to first point for next round of the loop to calculate distance
    x1 = x2
    y1 = y2
    
    
#connecting the last string and making the nail above the string
screw.goto(final_x, final_y)
screw.down()
screw.pencolor("red")
screw.goto(x_coord_1,y_coord_1)
screw.pencolor("blue")
screw.dot(5)
screw.up()
screw.goto(final_x, final_y)
screw.down()
screw.pencolor("blue")
screw.dot(5)

#adding the last string's distance
distance = math.sqrt((x_coord_1 - x1)**2 + (y_coord_1 - y1)**2)  
total_length = total_length + distance

#conversion from pixel to m
total_length = total_length/32

#calculation and print
board = 5
nails = 0.12
string = 0.07
total_nails = screw_num*nails
total_string = total_length*string
total = board + total_nails + total_string
total = round(total,2)
screw.pencolor("green")
print(total_length)
screw.write(f"Total Cost is ${total}", align="right", font=("Arial", 10, "bold"))

# Make a clean exit
screen.exitonclick() 
turtle.done()
