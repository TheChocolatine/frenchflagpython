def create_french_flag(width, height):
    # Define colors
    blue = (0, 85, 164)   # RGB for blue
    white = (255, 255, 255)   # RGB for white
    red = (239, 65, 53)   # RGB for red

    # Create a 2D array representing the flag
    flag = [[blue] * (width // 3) for _ in range(height)]
    for row in flag:
        row.extend([white] * (width // 3))
        row.extend([red] * (width // 3))

    # Print out the flag
    for row in flag:
        for pixel in row:
            print(f"\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m \033[0m", end='')
        print()

width = 30  # Adjust as needed
height = 15  # Adjust as needed
create_french_flag(width, height)
