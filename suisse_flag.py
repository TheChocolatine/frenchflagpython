def create_swiss_flag(width, height):
    # Define colors
    white = (255, 255, 255)   # RGB for white
    red = (213, 43, 30)   # RGB for red

    # Create a 2D array representing the flag
    flag = [[red] * width for _ in range(height)]
    
    # Define the size and position of the white cross
    cross_width = width // 5
    cross_height = height // 5
    cross_x = (width - cross_width) // 2
    cross_y = (height - cross_height) // 2

    # Draw the white cross
    for y in range(cross_y, cross_y + cross_height):
        for x in range(width):
            flag[y][x] = white
    for x in range(cross_x, cross_x + cross_width):
        for y in range(height):
            flag[y][x] = white

    # Print out the flag
    for row in flag:
        for pixel in row:
            print(f"\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m \033[0m", end='')
        print()

width = 20  # Adjust as needed
height = 10  # Adjust as needed
create_swiss_flag(width, height)
