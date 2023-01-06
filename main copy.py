from random import randint
from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
# canvas_width = int(input("Enter canvas width: "))
# canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white" : (255, 255, 255), "black" : (0, 0, 0)}
# canvas_color = input("\nEnter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(color=colors["black"])

while True:
    shape_type = input("\nWhat do you like to draw?(ENTER to quit): ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "r":
        rec_x = randint(20, 1280)
        rec_y = randint(20, 364)
        rec_width = randint(100, 200)
        rec_height = randint(50, 150)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        
        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)
    
    if shape_type.lower() == "s":
        sqr_x = randint(20, 1260)
        sqr_y = randint(20, 364)
        sqr_side = randint(50, 150)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        
        # Create the square
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)
        
    if shape_type == "":
        print("\nFarewell...!\n")
        break

canvas.make("./images/canvas.png")