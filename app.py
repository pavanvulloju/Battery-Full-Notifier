import sys
import time
import psutil
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

# Change the below value when you need to get the Notification Popup Box
# here it is set to 95 i.e, when your battery reaches 95, you get a popuup asking to uplug you PC
BATTERY_STOP_PERCENT = 95

while True:
	battery_status = psutil.sensors_battery()
	if battery_status.power_plugged:
		if battery_status.percent >= BATTERY_STOP_PERCENT:
			messagebox.showwarning("Battery Full", f"You might want to unplug your PC\n\n"
												f"Battery Percentage : { BATTERY_STOP_PERCENT}")
      # This runs only once as there is no Recursion, it can be updated for many times also
			sys.exit()
	else:

		time.sleep(600)  # It waits for 10 min to check charger is plugged-in or not
		# This is wait for system to check whether charger plugged-in or not

	# print(battery_status.percent)

	time.sleep(30)  # change it to 30  # For Testing Purposes set it to 3
	# This is the wait time when charger plugged-in to check battery percent time to time
