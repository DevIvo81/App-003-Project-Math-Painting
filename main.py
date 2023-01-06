from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white" : (255, 255, 255), "black" : (0, 0, 0)}
canvas_color = input("\nEnter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

while True:
    shape_type = input("\nWhat do you like to draw?(ENTER to quit): ")
    # Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("\nEnter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red?: "))
        green = int(input("How much green?: "))
        blue = int(input("How much blue?: "))
        
        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=(red, green, blue))
        r1.draw(canvas)
    
    if shape_type.lower() == "square":
        sqr_x = int(input("\nEnter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side of the square: "))
        red = int(input("How much red?: "))
        green = int(input("How much green?: "))
        blue = int(input("How much blue?: "))
        
        # Create the square
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)
        
    if shape_type == "":
        print("\nFarewell...!\n")
        break

canvas.make("./images/canvas.png")