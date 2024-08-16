import tkinter as tk
from PIL import Image, ImageTk

def update_x(value):
    x_value.set(f'X: {int(value)} deg')  # Display X value as an integer
    # Add code to send X value to the servo controlling the X axis

def update_y(value):
    y_value.set(f'Y: {int(value)} deg')  # Display Y value as an integer
    # Add code to send Y value to the servo controlling the Y axis

def move_to_home():
    x_value.set("X: 45 deg")
    y_value.set("Y: 45 deg")
    slider_x.set(45)
    slider_y.set(45)
    # Add code to send home position to the servos

# Create the main window
window = tk.Tk()
window.title("2R Robot Control")


window.geometry('800x800')

arm_img = Image.open("./miniproject/manipulator.jpg")
arm_img = arm_img.resize((300,300))
arm_img = ImageTk.PhotoImage(arm_img)  # Replace with your image file

# Create a label to hold the image
image_label = tk.Label(window, image=arm_img)
image_label.pack()

image = Image.open("/home/vinoth/robotcontrol/miniproject/home.png") # Load your jpg image
image = image.resize((20, 20))
home_icon = ImageTk.PhotoImage(image)

# Labels for displaying the current positions
x_value = tk.StringVar()
y_value = tk.StringVar()
x_value.set("X: 0 deg")
y_value.set("Y: 0 deg")

label_x = tk.Label(window, textvariable=x_value)
label_x.pack(pady=20)

label_y = tk.Label(window, textvariable=y_value)
label_y.pack()

# Sliders for X and Y axis control
slider_x = tk.Scale(window, from_=-100, to=100, orient='horizontal', command=update_x,width=20,length=400)
slider_x.pack(padx=40,pady=40)

slider_y = tk.Scale(window, from_=-100, to=100, orient='horizontal', command=update_y,width=20,length=400)
slider_y.pack(padx=40,pady=40)

# Create the Home button with the image
btn_home = tk.Button(window, text="Home", image=home_icon, compound=tk.LEFT, command=move_to_home)
btn_home.pack(pady=60)

# Start the Tkinter event loop
window.mainloop()
