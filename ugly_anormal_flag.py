def create_lgbt_flag(width, height):
    # Define colors
    red = (255, 0, 0)       # RGB for red
    orange = (255, 165, 0)  # RGB for orange
    yellow = (255, 255, 0)  # RGB for yellow
    green = (0, 128, 0)     # RGB for green
    blue = (0, 0, 255)      # RGB for blue
    purple = (128, 0, 128)  # RGB for purple

    # Calculate the width of each stripe
    stripe_width = width // 6

    # Create a list of colors for each stripe
    stripe_colors = [red, orange, yellow, green, blue, purple]

    # Create the flag image
    flag = [[(0, 0, 0)] * width for _ in range(height)]

    # Draw each stripe
    for i in range(6):
        for x in range(stripe_width * i, stripe_width * (i + 1)):
            for y in range(height):
                flag[y][x] = stripe_colors[i]

    # Print out the flag
    for row in flag:
        for pixel in row:
            print(f"\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m \033[0m", end='')
        print()

# Adjust width and height as needed
width = 60
height = 20
create_lgbt_flag(width, height)
