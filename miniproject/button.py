import tkinter as tk
from PIL import Image, ImageTk
# Variables to store the x and y positions
x_pos = 0
y_pos = 0

# Update and display the x and y positions
def update_x(delta):
    global x_pos
    x_pos += delta
    x_value.set(f'X: {x_pos}')
    # Add code to send the updated x_pos value to the servo

def update_y(delta):
    global y_pos
    y_pos += delta
    y_value.set(f'Y: {y_pos}')
    # Add code to send the updated y_pos value to the servo

# Set x and y to home position
def move_to_home():
    global x_pos, y_pos
    x_pos = 45  # Home x value
    y_pos = 45 # Home y value
    x_value.set(f'X: {x_pos}')
    y_value.set(f'Y: {y_pos}')
    # Add code to send the home position to the servos

# Create the main window
window = tk.Tk()
window.title("2R Robot Control")
image = Image.open("./miniproject/home.png") # Load your jpg image
image = image.resize((20, 20))
home_icon = ImageTk.PhotoImage(image)
# Labels to display current positions
x_value = tk.StringVar()
y_value = tk.StringVar()
x_value.set(f"X: {x_pos}")
y_value.set(f"Y: {y_pos}")

label_x = tk.Label(window, textvariable=x_value)
label_x.pack()

label_y = tk.Label(window, textvariable=y_value)
label_y.pack()

# Buttons for x-axis control
frame_x = tk.Frame(window)
frame_x.pack()

btn_x_minus = tk.Button(frame_x, text="X-", command=lambda: update_x(-1))
btn_x_minus.pack(side='left', padx=10)

btn_x_plus = tk.Button(frame_x, text="X+", command=lambda: update_x(1))
btn_x_plus.pack(side='right', padx=10)

# Buttons for y-axis control
frame_y = tk.Frame(window)
frame_y.pack()

btn_y_minus = tk.Button(frame_y, text="Y-", command=lambda: update_y(-1))
btn_y_minus.pack(side='left', padx=10)

btn_y_plus = tk.Button(frame_y, text="Y+", command=lambda: update_y(1))
btn_y_plus.pack(side='right', padx=10)

# Home button to reset to the home position
btn_home = tk.Button(window, text="Home",image=home_icon,compound=tk.LEFT, command=move_to_home)
btn_home.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()
