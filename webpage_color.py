import random

# Generate a random number between 1 and 5
color_choice = random.randint(1, 5)

# Set the background color based on the random number
if color_choice == 1:
    bg_color = "#FF4136"  # Red
elif color_choice == 2:
    bg_color = "#0074D9"  # Blue
elif color_choice == 3:
    bg_color = "#2ECC40"  # Green
elif color_choice == 4:
    bg_color = "#FFDC00"  # Yellow
else:
    bg_color = "#B10DC9"  # Purple

# Print the CSS code for setting the background color
print("background-color:", bg_color)
