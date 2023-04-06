import cv2
import numpy as np
import imutils
from tkinter import *

# Define the range of colors for fire
lower_fire = np.array([0,70,70], dtype = "uint8")
upper_fire = np.array([30,255,255], dtype = "uint8")

# Define the range of colors for smoke
lower_smoke = np.array([100,100,100], dtype = "uint8")
upper_smoke = np.array([120,255,255], dtype = "uint8")

# Start the video stream from the camera
camera = cv2.VideoCapture(0)

# Create a GUI window
root = Tk()
root.title("Fire and Smoke Detection")
root.geometry("500x500")

# Create a label to display the video frame
frame_label = Label(root)
frame_label.pack()

# Create a label to display the fire detection result
fire_label = Label(root, text = "Fire: Not Detected", font = ("Arial", 16))
fire_label.pack()

# Create a label to display the smoke detection result
smoke_label = Label(root, text = "Smoke: Not Detected", font = ("Arial", 16))
smoke_label.pack()

def detect_fire_smoke():
    grabbed, frame = camera.read()
    if not grabbed:
        return
        
    # Resize the frame to reduce processing time
    frame = imutils.resize(frame, width = 500)
    
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Detect fire using inRange function
    mask_fire = cv2.inRange(hsv, lower_fire, upper_fire)
    mask_fire = cv2.erode(mask_fire, None, iterations = 2)
    mask_fire = cv2.dilate(mask_fire, None, iterations = 2)
    cnts_fire = cv2.findContours(mask_fire.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts_fire = imutils.grab_contours(cnts_fire)
    
    # Detect smoke using inRange function
    mask_smoke = cv2.inRange(hsv, lower_smoke, upper_smoke)
    mask_smoke = cv2.erode(mask_smoke, None, iterations = 2)
    mask_smoke = cv2.dilate(mask_smoke, None, iterations = 2)
    cnts_smoke = cv2.findContours(mask_smoke.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts_smoke = imutils.grab_contours(cnts_smoke)
    
    # Update the fire detection result
    if len(cnts_fire) > 0:
        fire_detected = True
        fire_label.config(text = "Fire: Detected", font = ("Arial", 16), fg = "red")
    else:
        fire_detected = False
        fire_label.config(text = "Fire: Not Detected", font = ("Arial", 16), fg = "black")
    # Update the smoke detection result
    if len(cnts_smoke) > 0:
        smoke_detected = True
        smoke_label.config(text = "Smoke: Detected", font = ("Arial", 16), fg = "red")
    else:
        smoke_detected = False
        smoke_label.config(text = "Smoke: Not Detected", font = ("Arial", 16), fg = "black")

# Display the video frame
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
imgtk = ImageTk.PhotoImage(image = img)
frame_label.imgtk = imgtk
frame_label.configure(image = imgtk)
frame_label.after(10, detect_fire_smoke)
root.mainloop()

camera.release()
cv2.destroyAllWindows()