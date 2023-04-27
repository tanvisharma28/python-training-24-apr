import pyautogui
import time

# Set the duration for which you want to keep the screen awake in seconds
duration = 30 * 60

# Set the interval between each mouse click in seconds
interval = 5

# Get the current mouse position
x, y = pyautogui.position()

# Calculate the number of clicks needed to keep the screen awake for the specified duration
num_clicks = duration // interval

# Loop through and simulate mouse clicks
for i in range(num_clicks):
    # Move the mouse slightly to avoid the operating system detecting a stuck cursor
    pyautogui.moveTo(x + 1, y)
    pyautogui.moveTo(x, y)
    
    # Simulate a left mouse button click
    pyautogui.click(button='left')
    
    # Wait for the specified interval before simulating the next mouse click
    time.sleep(interval)
    print("xyz")
    print(30)